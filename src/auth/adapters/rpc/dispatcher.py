from typing import Callable, Dict


class RpcDispatcher:
    def __init__(self):
        self._handlers: Dict[str, Callable[[dict], dict]] = {}

    def register(self, queue_name: str, handler: Callable[[dict], dict]):
        self._handlers[queue_name] = handler
        return

    def get_handler(self, queue_name: str):
        return self._handlers.get(queue_name)

    def get_all_queues(self):
        return list(self._handlers.keys())
