from abc import abstractmethod
from typing import Protocol

from social_net.auth.models.user import User


class IdProvider(Protocol):
    @abstractmethod
    async def get_user(self) -> User:
        ...
