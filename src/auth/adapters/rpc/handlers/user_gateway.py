from uuid import UUID

from src.auth.adapters.gateway.user import UserGatewayImpl
from src.auth.adapters.rpc.dispatcher import RpcDispatcher
from src.auth.application.common.gateway.user import UserGateway
from src.auth.models.user import User


class UserGatewayHandler:
    gateway: UserGateway

    async def get_user_by_uuid(self, user_id: UUID) -> User | None:
        user = await self.gateway.get_by_id(user_id)

        if not user:
            return None

        return user

