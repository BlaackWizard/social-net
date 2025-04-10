from abc import abstractmethod
from typing import Protocol, Any


class UoW(Protocol):
    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def add(self, instance: Any) -> None: ...

    @abstractmethod
    async def delete(self, instance: Any) -> None: ...

