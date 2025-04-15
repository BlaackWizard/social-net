import uuid
from datetime import datetime, timedelta

from src.auth.application.common.gateway.user import UserGateway
from src.auth.application.common.jwt.access_token_processor import \
    AccessTokenProcessor
from src.auth.application.common.password_hasher import PasswordHasher
from src.auth.application.common.uow import UoW
from src.auth.application.dto.user import (AccessTokenDTO, TokenResponse,
                                           UserAuthorizeRequest)
from src.auth.application.errors.user_errors import UserNotFoundError
from src.auth.application.errors.user_request import InvalidPasswordError
from src.auth.models.user import User


class AuthorizeUser:
    def __init__(
        self,
        uow: UoW,
        user_gateway: UserGateway,
        password_hasher: PasswordHasher,
        access_token_processor: AccessTokenProcessor,
    ):
        self.uow = uow
        self.user_gateway = user_gateway
        self.ph = password_hasher
        self.token_processor = access_token_processor

    async def execute(self, data: UserAuthorizeRequest) -> TokenResponse:

        user: User | None = await self.user_gateway.get_by_email(str(data.email))

        if not user:
            raise UserNotFoundError

        valid_password = self.ph.check_password(data.password, user.hashed_password)

        if not valid_password:
            raise InvalidPasswordError

        await self.uow.commit()

        token_id = uuid.uuid4()
        exp = datetime.now() + timedelta(days=30)

        dto = AccessTokenDTO(
                uid=user.user_id,
                token_id=token_id,
                expires_in=exp,
            )
        access_token = self.token_processor.encode(
            dto.model_dump()
        )

        return TokenResponse(
            uid=user.user_id,
            access_token=access_token,
        )
