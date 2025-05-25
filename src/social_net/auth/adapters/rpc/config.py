from dataclasses import dataclass

from aio_pika.abc import AbstractConnection, AbstractChannel


@dataclass(frozen=True)
class RqConfig:
    connection: AbstractConnection
    channel: AbstractChannel

