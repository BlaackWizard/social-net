from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from social_net.subscription.models.subscription import SubscriptionModel


class SubscriptionGateway(Protocol):
    @abstractmethod
    async def get_subscription_by_user_and_follower_uuid(
        self,
        follower_id: UUID,
        user_id: UUID,
    ) -> SubscriptionModel | None:
        ...

    @abstractmethod
    async def get_all_followers_by_user_uuid(self, user_id: UUID) -> list[UUID]: ...

