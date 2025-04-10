from abc import abstractmethod
from typing import Protocol, TypeAlias, Any
import jwt
from dataclasses import dataclass

from src.auth.application.common.jwt.config import ConfigJWT
from src.auth.application.errors.jwt_errors import JWTDecodeError, JWTExpiredError

JWTPayload: TypeAlias = dict[str, Any]
JWTToken: TypeAlias = str

class JWTProcessor(Protocol):
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
        return jwt.encode(data, self.config.key, self.config.algorithm)

    def decode(self, token: JWTToken) -> JWTPayload:
        try:
            payload = jwt.decode(token, self.config.key, algorithms=[self.config.algorithm])
        except jwt.DecodeError:
            raise JWTDecodeError
        except jwt.ExpiredSignatureError as exc:
            raise JWTExpiredError from exc

        return payload
