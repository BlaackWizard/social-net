from typing import Protocol
from abc import abstractmethod
from uuid import UUID

from src.subscription.models.subscription import SubscriptionModel


class SubscriptionGateway(Protocol):
    @abstractmethod
    async def get_subscription_by_user_and_follower_uuid(
        self,
        follower_id: UUID,
        user_id: UUID
    ) -> SubscriptionModel | None: ...
