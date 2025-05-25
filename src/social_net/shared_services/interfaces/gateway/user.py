from typing import Protocol
from abc import abstractmethod
from uuid import UUID
from dataclasses import dataclass

@dataclass
class UserDTO:
    user_id: UUID
    username: str
    email: str
    is_active: bool

class SharedUserGateway(Protocol):
    @abstractmethod
    async def get_user_by_uuid(self, user_id: UUID) -> UserDTO | None: ...
