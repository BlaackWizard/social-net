from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from social_net.auth.application.common.gateway.user import UserGateway
from social_net.auth.models.user import User


@dataclass
class UserGatewayImpl(UserGateway): # type: ignore[misc]
    session: AsyncSession

    async def get_by_id(self, user_id: UUID) -> User | None:
        q = select(User).where(User.user_id == user_id)

        res = await self.session.execute(q)

        return res.scalar()

    async def get_by_username(self, username: str) -> User | None:
        q = select(User).where(User.username == username)

        res = await self.session.execute(q)

        return res.scalar()

    async def get_by_email(self, email: str) -> User | None:
        q = select(User).where(User.email == email)

        res = await self.session.execute(q)

        return res.scalar()
