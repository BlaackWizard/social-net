import jwt
from uuid import UUID
from dataclasses import dataclass
from src.auth.application.common.jwt.config import ConfigJWT

@dataclass
class TokenEncoder:
    config: ConfigJWT

    def decrypt(self, token: str) -> UUID:
        return jwt.decode(token, self.config.key, algorithms=[self.config.algorithm])['uid']
