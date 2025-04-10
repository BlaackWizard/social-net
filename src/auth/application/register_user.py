import uuid
from datetime import datetime, timedelta

from src.auth.application.common.gateway.user import UserGateway
from src.auth.application.common.jwt.confirmation_token_processor import ConfirmationTokenProcessor
from src.auth.application.common.password_hasher import PasswordHasher
from src.auth.application.common.token_sender import TokenSender
from src.auth.application.common.uow import UoW
from src.auth.application.dto.user import UserRegisterRequest, UserConfirmationTokenDTO, UserRegisterResponse
from src.auth.application.errors.user_request import UserAlreadyExistsWithThisEmailError, UserNameIsOccupiedError
from src.auth.models.user import User


class RegisterUser:
    def __init__(
            self,
            token_processor: ConfirmationTokenProcessor,
            user_gateway: UserGateway,
            password_hasher: PasswordHasher,
            uow: UoW,
            token_sender: TokenSender
        ):
        self.token_processor = token_processor
        self.user_gateway = user_gateway
        self.password_hasher = password_hasher
        self.token_sender = token_sender
        self.uow = uow

    async def execute(self, data: UserRegisterRequest) -> UserRegisterResponse:
        check_exists_by_email = await self.user_gateway.get_by_email(str(data.email))
        check_exists_by_username = await self.user_gateway.get_by_username(data.username)

        if check_exists_by_email:
            raise UserAlreadyExistsWithThisEmailError

        if check_exists_by_username:
            raise UserNameIsOccupiedError

        hashed_password = self.password_hasher.hash_password(data.password2)

        user = User(
            username=data.username,
            email=str(data.email),
            hashed_password=hashed_password
        )

        await self.uow.add(user)

        exp = datetime.now() + timedelta(hours=3)
        token_id = uuid.uuid4()

        self.token_sender.send(
            UserConfirmationTokenDTO(
                uid=user.user_id,
                token_id=token_id,
                expires_in=exp
            ),
            user_email=user.email
        )
        await self.uow.commit()
        return UserRegisterResponse(
            message=f"Подтвердите свою почту: {data.email}, мы выслали вам на почту письмо"
        )
