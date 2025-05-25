from dataclasses import dataclass

from social_net.auth.application.common.id_provider import IdProvider
from social_net.auth.application.dto.user import UserInfoResponse


@dataclass
class Me:
    id_provider: IdProvider

    async def execute(self) -> UserInfoResponse:
        result = await self.id_provider.get_user()

        return UserInfoResponse(
            uid=result.user_id,
            username=result.username,
            email=result.email
        )
