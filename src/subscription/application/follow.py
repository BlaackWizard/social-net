from dataclasses import dataclass
from uuid import UUID

from src.subscription.application.common.gateway import SubscriptionGateway
from src.subscription.application.common.id_provider import IdProvider
from src.subscription.application.common.uow import UoW
from src.subscription.application.exceptions.subscription import SubscriptionAlreadyExists, NotFoundUserError
from src.subscription.models.subscription import SubscriptionModel


@dataclass
class FollowRequest:
    user_id: UUID

@dataclass(frozen=True, slots=True)
class Follow:
    uow: UoW
    subscription_gateway: SubscriptionGateway
    id_provider: IdProvider

    async def execute(self, data: FollowRequest) -> None:
        follower_id = await self.id_provider.get_follower_user_uuid()
        if not follower_id:
            raise NotFoundUserError

        subscription_exists = await self.subscription_gateway.get_subscription_by_user_and_follower_uuid(
            follower_id=follower_id,
            user_id=data.user_id,
        )

        if subscription_exists:
            raise SubscriptionAlreadyExists

        subscription = SubscriptionModel(
            user_id=data.user_id,
            follower_id=follower_id
        )

        await self.uow.add(instance=subscription)
        await self.uow.commit()

        return