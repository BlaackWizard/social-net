import asyncio
import json
import uuid
from typing import MutableMapping, Any, Dict

from aio_pika import Message
from aio_pika.abc import AbstractIncomingMessage

from social_net.auth.adapters.rpc.base.rpc_client import BaseRpcClient
from social_net.auth.adapters.rpc.config import RqConfig


class RQRpcClient(BaseRpcClient): # type: ignore[misc]
    def __init__(self, rq_config: RqConfig, queue_name: str) -> None:
        self.queue_name = queue_name
        self.callback_queue = None
        self.connection = rq_config.connection
        self.channel = rq_config.channel
        self.futures: MutableMapping[str, asyncio.Future[Any]] = {}

    async def _on_response(self, message: AbstractIncomingMessage) -> None:
        async with message.process():
            body = json.loads(message.body.decode())
            correlation_id = message.correlation_id

            if correlation_id in self.futures:
                future = self.futures.pop(correlation_id)
                future.set_result(body)

    async def call(self, payload: Dict[str, Any]) -> Any:
        correlation_id = str(uuid.uuid4())
        loop = asyncio.get_running_loop()
        future = loop.create_future()

        self.futures[correlation_id] = future

        message = Message(
            body=json.dumps(payload).encode(),
            correlation_id=correlation_id,
            reply_to=self.callback_queue
        )
        await self.channel.default_exchange.publish(
            message, routing_key=self.queue_name
        )
        return await future
