from dataclasses import dataclass
from uuid import UUID

import jwt

from src.auth.application.common.jwt.config import ConfigJWT


@dataclass
class TokenEncoder:
    config: ConfigJWT

    def decrypt(self, token: str) -> UUID:
        return jwt.decode(token, self.config.key, algorithms=[self.config.algorithm])[
            'uid'
        ]
