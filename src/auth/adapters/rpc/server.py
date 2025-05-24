import json

from aio_pika.abc import AbstractIncomingMessage

from src.auth.adapters.rpc.base.rpc_server import BaseRpcServer
from src.auth.adapters.rpc.config import RqConfig
from src.auth.adapters.rpc.dispatcher import RpcDispatcher
from aio_pika import Message


class RQRpcServer(BaseRpcServer):
    def __init__(self, config: RqConfig, dispatcher: RpcDispatcher):
        self.connection = config.connection
        self.channel = config.channel
        self.dispatcher = dispatcher

    async def connect(self):
        for queue_name in self.dispatcher.get_all_queues():
            queue = await self.channel.declare_queue(durable=True)
            await queue.consume(self._on_request(queue_name))

    def _on_request(self, queue_name: str):
        async def handler(message: AbstractIncomingMessage):
            async with message.process():
                handler = self.dispatcher.get_handler(queue_name)
                payload = json.loads(message.body.decode())

                if not handler:
                    raise NotFoundHandlerError
                response = await handler(payload)

                msg = Message(
                    json.dumps(response).encode(),
                    correlation_id=message.correlation_id,
                )
                await self.channel.default_exchange.publish(
                    msg, routing_key=message.reply_to
                )
        return handler
