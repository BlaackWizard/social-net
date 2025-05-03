from typing import Protocol
from abc import abstractmethod

class IdProvider(Protocol):
    @abstractmethod
    async def get_follower_user_uuid(self): ...
