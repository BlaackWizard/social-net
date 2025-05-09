from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.subscription.application.common.gateway import SubscriptionGateway
from src.subscription.models.subscription import SubscriptionModel


@dataclass
class SubscriptionGatewayImpl(SubscriptionGateway):
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
