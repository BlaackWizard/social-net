from datetime import datetime

from src.auth.application.common.jwt.config import ConfigJWT
from src.auth.application.common.jwt.token_processor import JWTProcessor, JWTToken
from src.auth.application.dto.user import AccessTokenDTO
from src.auth.application.errors.jwt_errors import JWTDecodeError, AccessTokenСorruptedError
import jwt

class AccessTokenProcessor(JWTProcessor):
    config: ConfigJWT

    def encode(self, data: AccessTokenDTO) -> JWTToken:
        payload = {
            'sub': {
                'uid': data.uid,
                'token_id': data.token_id
            },
            'exp': str(data.expires_in)
        }
        return jwt.encode(payload, self.config.key, self.config.algorithm)

    def decode(self, token: JWTToken) -> AccessTokenDTO:
        try:
            payload = jwt.decode(token, self.config.key, algorithms=[self.config.algorithm])

            sub = payload['sub']
            exp = datetime.strptime(payload['exp'], "%y/%m/%d/%h/%m")

            uid = sub['uid']
            token_id = sub['token_id']

            dto = AccessTokenDTO(
                expires_in=exp,
                uid=uid,
                token_id=token_id
            )
        except (JWTDecodeError, TypeError, KeyError, ValueError):
            raise AccessTokenСorruptedError

        return dto
