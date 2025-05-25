from typing import Callable, Dict, List


from typing import Optional, Any


class RpcDispatcher:
    def __init__(self) -> None:
        self._handlers: Dict[str, Callable[[Dict[str, Any]], Dict[str, Any]]] = {}

    def register(self, queue_name: str, handler: Callable[[Dict[str, Any]], Dict[str, Any]]) -> None:
        self._handlers[queue_name] = handler

    def get_handler(self, queue_name: str) -> Optional[Callable[[Dict[str, Any]], Dict[str, Any]]]:
        return self._handlers.get(queue_name)

    def get_all_queues(self) -> List[str]:
        return list(self._handlers.keys())

