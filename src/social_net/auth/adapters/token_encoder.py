from dataclasses import dataclass
from uuid import UUID

import jwt

from social_net.auth.application.common.jwt.config import ConfigJWT


@dataclass
class TokenEncoder:
    config: ConfigJWT

    def decrypt(self, token: str) -> UUID:
        return UUID(jwt.decode(token, self.config.key, algorithms=[self.config.algorithm])[
            'uid'
        ])
