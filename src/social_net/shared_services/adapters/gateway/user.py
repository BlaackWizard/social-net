from typing import Annotated
from uuid import UUID

from dishka import FromComponent

from social_net.shared_services.interfaces.gateway.user import UserDTO, SharedUserGateway
from social_net.auth.application.common.gateway.user import UserGateway
from dataclasses import dataclass

@dataclass
class SharedUserGatewayImpl(SharedUserGateway): # type: ignore[misc]
    gateway: Annotated[UserGateway, FromComponent("auth")]

    async def get_user_by_uuid(self, user_id: UUID) -> UserDTO | None:
        user = await self.gateway.get_by_id(user_id)

        if not user:
            return None

        return UserDTO(
            user_id=user.user_id,
            username=user.username,
            email=user.email,
            is_active=user.is_active
        )
