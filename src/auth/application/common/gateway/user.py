from abc import abstractmethod
from typing import Protocol, TypeAlias
from uuid import UUID

from src.auth.models.user import User

user_id: TypeAlias = UUID


class UserGateway(Protocol):
    @abstractmethod
    async def get_by_id(self, user_id: UUID) -> User | None:
        ...

    @abstractmethod
    async def get_by_username(self, username: str) -> User | None:
        ...

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None:
        ...
