from aio_pika.abc import AbstractIncomingMessage
from typing import Protocol
from abc import abstractmethod


class BaseRpcServer(Protocol):
    @abstractmethod
    async def handle(self, message: AbstractIncomingMessage): ...
