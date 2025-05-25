from dataclasses import dataclass

from social_net.shared_services.interfaces.gateway.user import SharedUserGateway
from social_net.subscription.application.common.gateway import SubscriptionGateway
from social_net.subscription.application.common.id_provider import IdProvider

from social_net.subscription.application.common.uow import UoW
from social_net.subscription.application.dto import UnFollowRequest
from social_net.subscription.application.exceptions.subscription import NotFoundUserError, SubscriptionNotExistsError


@dataclass
class UnFollow:
    subscription_gateway: SubscriptionGateway
    id_provider: IdProvider
    user_gateway: SharedUserGateway
    uow: UoW

    async def execute(self, data: UnFollowRequest) -> None:
        user = await self.user_gateway.get_user_by_uuid(data.user_id)
        follower_id = await self.id_provider.get_follower_user_uuid()

        if not user:
            raise NotFoundUserError

        subscription = await self.subscription_gateway.get_subscription_by_user_and_follower_uuid(
            follower_id=follower_id,
            user_id=user.user_id
        )

        if not subscription:
            raise SubscriptionNotExistsError

        await self.uow.delete(subscription)
        await self.uow.commit()
        return
