from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseRpcClient(ABC):
    @abstractmethod
    async def call(self, payload: Dict[str, Any]) -> Any:
        pass

