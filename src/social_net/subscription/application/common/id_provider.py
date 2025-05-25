from abc import abstractmethod, ABC
from uuid import UUID


class IdProvider(ABC):
    @abstractmethod
    async def get_follower_user_uuid(self) -> UUID | None:
        ...
