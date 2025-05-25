from dataclasses import dataclass
from typing import List
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from social_net.subscription.application.common.gateway import SubscriptionGateway
from social_net.subscription.models.subscription import SubscriptionModel


@dataclass
class SubscriptionGatewayImpl(SubscriptionGateway): # type: ignore[misc]
    session: AsyncSession

    async def get_subscription_by_user_and_follower_uuid(
        self,
        follower_id: UUID,
        user_id: UUID,
    ) -> SubscriptionModel | None:
        q = select(SubscriptionModel).where(
            SubscriptionModel.user_id == user_id,
            SubscriptionModel.follower_id == follower_id,
        )

        result = await self.session.execute(q)

        if result:
            return result.scalar()
        return None

    async def get_all_followers_by_user_uuid(self, user_id: UUID) -> List[UUID]:
        q = select(SubscriptionModel.follower_id).where(
            SubscriptionModel.user_id == user_id
        )

        result = await self.session.execute(q)

        return list(result.scalars().all())

