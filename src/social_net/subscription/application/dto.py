from dataclasses import dataclass
from uuid import UUID


@dataclass
class SubscriptionRequest:
    user_id: UUID
@dataclass
class FollowRequest(SubscriptionRequest): ...

@dataclass
class UnFollowRequest(SubscriptionRequest): ...

@dataclass
class AllFollowersRequest(SubscriptionRequest): ...
