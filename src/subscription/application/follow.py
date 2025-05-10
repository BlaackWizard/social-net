from dataclasses import dataclass
from uuid import UUID

from src.shared_services.interfaces.gateway.user import SharedUserGateway
from src.subscription.application.common.gateway import SubscriptionGateway
from src.subscription.application.common.id_provider import IdProvider
from src.subscription.application.common.uow import UoW
from src.subscription.application.exceptions.subscription import (
    FollowSelfForbidden, NotFoundUserError, SubscriptionAlreadyExists)
from src.subscription.models.subscription import SubscriptionModel

@dataclass
class SubscriptionRequest():
    user_id: UUID
@dataclass
class FollowRequest(SubscriptionRequest): ...

@dataclass
class UnFollowRequest(SubscriptionRequest): ...

@dataclass
class AllFollowersRequest(SubscriptionRequest): ...


@dataclass(frozen=True, slots=True)
class Follow:
    uow: UoW
    subscription_gateway: SubscriptionGateway
    id_provider: IdProvider
    user_gateway: SharedUserGateway

    async def execute(self, data: FollowRequest) -> None:
        follower_id = await self.id_provider.get_follower_user_uuid()
        if not follower_id:
            raise NotFoundUserError

        user = await self.user_gateway.get_user_by_uuid(data.user_id)

        subscription_exists = (
            await self.subscription_gateway.get_subscription_by_user_and_follower_uuid(
                follower_id=follower_id,
                user_id=data.user_id,
            )
        )

        if not user:
            raise NotFoundUserError
        if data.user_id == follower_id:
            raise FollowSelfForbidden
        if subscription_exists:
            raise SubscriptionAlreadyExists

        subscription = SubscriptionModel(
            user_id=data.user_id,
            follower_id=follower_id,
        )

        await self.uow.add(instance=subscription)
        await self.uow.commit()

        return
