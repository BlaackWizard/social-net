from dataclasses import dataclass

@dataclass(frozen=True)
class SubscriptionException(Exception):
    message: str
