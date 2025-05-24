from abc import abstractmethod
from typing import Protocol, Any


class BaseRpcClient(Protocol):
    @abstractmethod
    async def call(self, payload: dict) -> Any:
        pass

