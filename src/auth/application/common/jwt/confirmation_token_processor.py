from dataclasses import dataclass
from datetime import datetime

import jwt

from src.auth.application.common.jwt.config import ConfigJWT
from src.auth.application.common.jwt.token_processor import (JWTPayload,
                                                             JWTProcessor,
                                                             JWTToken)
from src.auth.application.dto.user import UserConfirmationTokenDTO
from src.auth.application.errors.jwt_errors import (
    ConfirmationTokenСorruptedError, JWTDecodeError)


@dataclass
class ConfirmationTokenProcessor(JWTProcessor):
    config: ConfigJWT

    def encode(self, data: JWTPayload) -> JWTToken:
        payload = {
            'sub': {
                'uid': data['uid'],
                'token_id': data['token_id'],
            },
            'exp': str(data['expires_in']),
        }
        return jwt.encode(payload, self.config.key, self.config.algorithm)

    def decode(self, token: JWTToken) -> JWTPayload:
        try:
            payload = jwt.decode(
                token,
                self.config.key,
                algorithms=[self.config.algorithm],
            )

            sub = payload['sub']
            exp = datetime.strptime(payload['exp'], "%y/%m/%d/%h/%m")

            uid = sub['uid']
            token_id = sub['token_id']

            dto = UserConfirmationTokenDTO(
                expires_in=exp,
                uid=uid,
                token_id=token_id,
            )
        except (JWTDecodeError, TypeError, KeyError, ValueError):
            raise ConfirmationTokenСorruptedError

        return dto.model_dump()
