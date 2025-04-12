import uuid
from datetime import datetime, timedelta

from src.auth.application.common.gateway.user import UserGateway
from src.auth.application.common.jwt.access_token_processor import \
    AccessTokenProcessor
from src.auth.application.common.jwt.confirmation_token_processor import \
    ConfirmationTokenProcessor
from src.auth.application.common.uow import UoW
from src.auth.application.dto.user import AccessTokenDTO, TokenResponse
from src.auth.application.errors.jwt_errors import (JWTDecodeError,
                                                    JWTExpiredError)
from src.auth.application.errors.user_errors import UserNotFoundError
from src.auth.application.errors.user_request import UnauthorizedError


class VerifyUser:
    def __init__(
        self,
        token_processor: ConfirmationTokenProcessor,
        user_gateway: UserGateway,
        uow: UoW,
        access_token_processor: AccessTokenProcessor,
    ):
        self.uow = uow
        self.user_gateway = user_gateway
        self.token_processor = token_processor
        self.access_token_processor = access_token_processor

    async def execute(self, token: str):
        try:
            data = self.token_processor.decode(token)
        except (JWTDecodeError, JWTExpiredError, ValueError, TypeError, KeyError):
            raise UnauthorizedError

        user = await self.user_gateway.get_by_id(data['user_id'])

        if not user:
            raise UserNotFoundError

        user.is_active = True
        await self.uow.add(user)

        exp = datetime.now() + timedelta(days=30)

        token_id = uuid.uuid4()
        access_token = self.access_token_processor.encode(
            AccessTokenDTO(
                uid=user.user_id,
                expires_in=exp,
                token_id=token_id,
            ),
        )
        token = TokenResponse(
            access_token=access_token,
            uid=user.user_id,
        )

        await self.uow.commit()

        return token
