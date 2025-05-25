from dataclasses import dataclass
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from social_net.subscription.application.common.uow import UoW


@dataclass
class UoWS(UoW): # type: ignore[misc]
    session: AsyncSession

    async def commit(self) -> None:
        await self.session.commit()

    async def add(self, instance: Any) -> None:
        self.session.add(instance)

    async def delete(self, instance: Any) -> None:
        await self.session.delete(instance)
