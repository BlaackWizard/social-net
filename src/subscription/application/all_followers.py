from dataclasses import dataclass

from src.shared_services.interfaces.gateway.user import SharedUserGateway
from src.subscription.application.common.gateway import SubscriptionGateway
from uuid import UUID

from src.subscription.application.dto import AllFollowersRequest
from src.subscription.application.exceptions.subscription import NotFoundUserError


@dataclass
class AllFollowers:
    subscription_gateway: SubscriptionGateway
    user_gateway: SharedUserGateway

    async def execute(self, data: AllFollowersRequest) -> list[UUID]:
        user = await self.user_gateway.get_user_by_uuid(data.user_id)

        if not user:
            raise NotFoundUserError

        users = await self.subscription_gateway.get_all_followers_by_user_uuid(user.user_id)

        return users
