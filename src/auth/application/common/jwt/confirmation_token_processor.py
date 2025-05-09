from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

import jwt

from src.auth.application.common.jwt.config import ConfigJWT
from src.auth.application.common.jwt.token_processor import (JWTPayload,
                                                             JWTProcessor,
                                                             JWTToken)
from src.auth.application.dto.user import UserConfirmationTokenDTO
from src.auth.application.errors.jwt_errors import \
    ConfirmationTokenСorruptedError


@dataclass
class ConfirmationTokenProcessor(JWTProcessor):
    config: ConfigJWT

    def encode(self, data: JWTPayload) -> JWTToken:
        payload = {
            'exp': int(data['expires_in'].timestamp()),
            'uid': str(data['uid']),
            'token_id': str(data['token_id']),
        }
        return jwt.encode(payload, self.config.key, self.config.algorithm)

    def decode(self, token: JWTToken) -> JWTPayload:
        try:
            payload = jwt.decode(
                token,
                self.config.key,
                algorithms=[self.config.algorithm],
            )

            exp = datetime.fromtimestamp(payload['exp'])

            dto = UserConfirmationTokenDTO(
                expires_in=exp,
                uid=UUID(payload['uid']),
                token_id=UUID(payload['token_id']),
            )
        except (jwt.DecodeError, TypeError, KeyError, ValueError):
            raise ConfirmationTokenСorruptedError

        return dto.model_dump()
