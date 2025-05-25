from abc import abstractmethod, ABC
from typing import TypeAlias
from uuid import UUID

from social_net.auth.models.user import User

user_id: TypeAlias = UUID


class UserGateway(ABC):
    @abstractmethod
    async def get_by_id(self, user_id: UUID) -> User | None:
        ...

    @abstractmethod
    async def get_by_username(self, username: str) -> User | None:
        ...

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None:
        ...
