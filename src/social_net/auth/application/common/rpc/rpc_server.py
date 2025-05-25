from aio_pika.abc import AbstractIncomingMessage
from abc import abstractmethod, ABC


class BaseRpcServer(ABC):
    @abstractmethod
    async def handle(self, message: AbstractIncomingMessage) -> None: ...
