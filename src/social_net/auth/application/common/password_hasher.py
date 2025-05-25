from abc import abstractmethod
from typing import Protocol, TypeAlias

HASHED_PASSWORD: TypeAlias = str


class PasswordHasher(Protocol):
    @abstractmethod
    def hash_password(self, password: str) -> HASHED_PASSWORD:
        ...

    @abstractmethod
    def check_password(self, password: str, hashed_password: HASHED_PASSWORD) -> bool:
        ...
