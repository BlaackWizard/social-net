from dataclasses import dataclass
from typing import cast
from uuid import UUID

from fastapi import Request
from jwt.exceptions import PyJWTError

from social_net.auth.adapters.token_encoder import TokenEncoder
from social_net.auth.application.common.gateway.user import UserGateway
from social_net.auth.application.errors.user_request import UnauthorizedError
from social_net.auth.models.user import User

TOKEN_TYPE = 'Bearer'
AUTH_HEADER = "Authorization"
BEARER_SECTIONS = 2


@dataclass(frozen=True, slots=True)
class TokenBearerIdProvider:
    request: Request
    token_encoder: TokenEncoder

    def get_user_uuid(self) -> UUID | None:
        auth_header = self.request.headers.get(AUTH_HEADER)
        token: str | None = None

        if auth_header:
            parts = auth_header.split(" ")
            if len(parts) == BEARER_SECTIONS:
                token_type, token_value = parts
                if token_type == TOKEN_TYPE:
                    token = token_value

        if token is None:
            token = self.request.cookies.get("access_token")

        if not token:
            raise UnauthorizedError

        try:
            return cast(UUID, self.token_encoder.decrypt(token))
        except (PyJWTError, TypeError, ValueError, KeyError) as exc:
            raise UnauthorizedError from exc


@dataclass
class TokenProvider:
    _token_parser: TokenBearerIdProvider
    _user_gateway: UserGateway
    uid = None

    async def _authorize_user(self) -> UUID | None:
        return self._token_parser.get_user_uuid()

    async def get_user(self) -> User:
        user_id = self.uid or await self._authorize_user()

        user = await self._user_gateway.get_by_id(user_id)
        if not user:
            raise UnauthorizedError
        if not user.is_active:
            raise UnauthorizedError
        return user
