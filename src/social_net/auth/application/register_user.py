import uuid
from datetime import datetime, timedelta

from social_net.auth.application.common.gateway.user import UserGateway
from social_net.auth.application.common.jwt.confirmation_token_processor import \
    ConfirmationTokenProcessor
from social_net.auth.application.common.password_hasher import PasswordHasher
from social_net.auth.application.common.token_sender import TokenSender
from social_net.auth.application.common.uow import UoW
from social_net.auth.application.dto.user import (UserConfirmationTokenDTO,
                                           UserRegisterRequest,
                                           UserRegisterResponse)
from social_net.auth.application.errors.user_request import (
    UserAlreadyExistsWithThisEmailError, UserNameIsOccupiedError)
from social_net.auth.models.user import User


class RegisterUser:
    def __init__(
        self,
        token_processor: ConfirmationTokenProcessor,
        user_gateway: UserGateway,
        password_hasher: PasswordHasher,
        uow: UoW,
        token_sender: TokenSender,
    ):
        self.token_processor = token_processor
        self.user_gateway = user_gateway
        self.password_hasher = password_hasher
        self.token_sender = token_sender
        self.uow = uow

    async def execute(self, data: UserRegisterRequest) -> UserRegisterResponse:
        user_email = await self.user_gateway.get_by_email(str(data.email))
        user_username = await self.user_gateway.get_by_username(
            data.username,
        )

        if user_email:
            raise UserAlreadyExistsWithThisEmailError

        if user_username:
            raise UserNameIsOccupiedError

        hashed_password = self.password_hasher.hash_password(data.password2)
        uid = uuid.uuid4()
        user = User(
            username=data.username,
            email=str(data.email),
            hashed_password=hashed_password,
            user_id=uid,
        )

        self.uow.add(user)

        exp = datetime.now() + timedelta(hours=3)
        token_id = uuid.uuid4()

        self.token_sender.send(
            UserConfirmationTokenDTO(
                uid=user.user_id,
                token_id=token_id,
                expires_in=exp,
            ),
            user_email=str(data.email),
        )
        await self.uow.commit()
        return UserRegisterResponse(
            message=f"Подтвердите свою почту: {data.email}, мы выслали вам на почту письмо."
                    f"Срок подтверждения 3 часа.",
        )
