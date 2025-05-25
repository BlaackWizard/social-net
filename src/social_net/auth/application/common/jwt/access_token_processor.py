from dataclasses import dataclass
from datetime import datetime

import jwt

from social_net.auth.application.common.jwt.config import ConfigJWT
from social_net.auth.application.common.jwt.token_processor import (JWTPayload,
                                                             JWTProcessor,
                                                             JWTToken)
from social_net.auth.application.dto.user import AccessTokenDTO
from social_net.auth.application.errors.jwt_errors import (AccessTokenСorruptedError,
                                                    JWTDecodeError)


@dataclass
class AccessTokenProcessor(JWTProcessor): # type: ignore[misc]
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

            exp = datetime.strptime(payload['exp'], "%y/%m/%d")

            uid = payload['uid']
            token_id = payload['token_id']

            dto = AccessTokenDTO(
                expires_in=exp,
                uid=uid,
                token_id=token_id,
            )
        except (JWTDecodeError, TypeError, KeyError, ValueError):
            raise AccessTokenСorruptedError

        return dto.model_dump()
