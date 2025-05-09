from abc import abstractmethod
from typing import Protocol


class IdProvider(Protocol):
    @abstractmethod
    async def get_follower_user_uuid(self):
        ...
