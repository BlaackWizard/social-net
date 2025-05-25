from abc import abstractmethod, ABC
from typing import Any


class UoW(ABC):
    @abstractmethod
    async def add(self, instance: Any) -> None:
        ...

    @abstractmethod
    async def delete(self, instance: Any) -> None:
        ...

    @abstractmethod
    async def commit(self) -> None:
        ...
