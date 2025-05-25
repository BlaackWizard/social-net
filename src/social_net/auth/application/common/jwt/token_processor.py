from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Any, TypeAlias, Dict
from typing import cast

import jwt

from social_net.auth.application.common.jwt.config import ConfigJWT
from social_net.auth.application.errors.jwt_errors import (JWTDecodeError,
                                                    JWTExpiredError)

JWTPayload: TypeAlias = Dict[str, Any]
JWTToken: TypeAlias = str


class JWTProcessor(ABC):
    @abstractmethod
    def encode(self, data: JWTPayload) -> JWTToken:
        ...

    @abstractmethod
    def decode(self, token: JWTToken) -> JWTPayload:
        ...



@dataclass
class PyTokenProcessor(JWTProcessor):
    config: ConfigJWT

    def encode(self, data: JWTPayload) -> JWTToken:
        token = jwt.encode(data, self.config.key, self.config.algorithm)
        if isinstance(token, bytes):
            return token.decode('utf-8')
        return str(token)

    def decode(self, token: JWTToken) -> JWTPayload:
        try:
            payload = jwt.decode(
                token,
                self.config.key,
                algorithms=[self.config.algorithm],
            )
        except jwt.DecodeError:
            raise JWTDecodeError
        except jwt.ExpiredSignatureError as exc:
            raise JWTExpiredError from exc

        return cast(JWTPayload, payload)
