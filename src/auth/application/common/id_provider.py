from typing import Protocol
from abc import abstractmethod

from src.auth.models.user import User


class IdProvider(Protocol):
    @abstractmethod
    async def get_user(self) -> User: ...
