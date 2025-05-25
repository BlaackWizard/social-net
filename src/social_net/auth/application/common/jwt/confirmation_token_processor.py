from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

import jwt

from social_net.auth.application.common.jwt.config import ConfigJWT
from social_net.auth.application.common.jwt.token_processor import (JWTPayload,
                                                             JWTProcessor,
                                                             JWTToken)
from social_net.auth.application.dto.user import UserConfirmationTokenDTO
from social_net.auth.application.errors.jwt_errors import \
    ConfirmationTokenСorruptedError, ConfirmationTokenExpiredError


@dataclass
class ConfirmationTokenProcessor(JWTProcessor): # type: ignore[misc]
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

        except jwt.ExpiredSignatureError:
            raise ConfirmationTokenExpiredError
        return dto.model_dump()
