from src.auth.application.common.gateway.user import UserGateway
from src.auth.models.user import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from dataclasses import dataclass
from uuid import UUID

@dataclass
class UserGatewayImpl(UserGateway):
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
