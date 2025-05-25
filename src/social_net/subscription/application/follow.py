from dataclasses import dataclass

from social_net.shared_services.interfaces.gateway.user import SharedUserGateway
from social_net.subscription.application.common.gateway import SubscriptionGateway
from social_net.subscription.application.common.id_provider import IdProvider
from social_net.subscription.application.common.uow import UoW
from social_net.subscription.application.dto import FollowRequest
from social_net.subscription.application.exceptions.subscription import (
    FollowSelfForbidden, NotFoundUserError, SubscriptionAlreadyExists)
from social_net.subscription.models.subscription import SubscriptionModel


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
