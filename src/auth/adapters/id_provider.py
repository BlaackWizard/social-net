from dataclasses import dataclass
from uuid import UUID

from fastapi import Request
from jwt.exceptions import PyJWTError

from src.auth.adapters.token_encoder import TokenEncoder
from src.auth.application.common.gateway.user import UserGateway
from src.auth.application.errors.user_request import UnauthorizedError
from src.auth.models.user import User

TOKEN_TYPE = 'Bearer'
AUTH_HEADER = "Authorization"
BEARER_SECTIONS = 2


@dataclass(frozen=True, slots=True)
class TokenBearerIdProvider:
    request: Request
    token_encoder: TokenEncoder

    def get_user_uuid(self) -> UUID:
        auth_header = self.request.headers.get(AUTH_HEADER)
        if not auth_header:
            raise UnauthorizedError

        parts = auth_header.split(" ")
        if len(parts) != BEARER_SECTIONS:
            raise UnauthorizedError

        token_type, token = parts
        if token_type != TOKEN_TYPE:
            raise UnauthorizedError

        try:
            return self.token_encoder.decrypt(token)
        except (PyJWTError, TypeError, ValueError, KeyError) as exc:
            raise UnauthorizedError from exc


@dataclass
class TokenProvider:
    _token_parser: TokenBearerIdProvider
    _user_gateway: UserGateway
    uid = None

    async def _authorize_user(self) -> UUID:
        return self._token_parser.get_user_uuid()

    async def get_user(self) -> User:
        user_id = self.uid or await self._authorize_user()

        user = await self._user_gateway.get_by_id(user_id)
        if not user or user.is_active != True:
            raise UnauthorizedError

        return user
