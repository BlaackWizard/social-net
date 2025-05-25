from uuid import UUID

from sqlalchemy import Integer, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from social_net.subscription.models.base import Base


class SubscriptionModel(Base): # type: ignore[misc]
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # noqa
    follower_id: Mapped[UUID] = mapped_column(Uuid, nullable=False)
    user_id: Mapped[UUID] = mapped_column(Uuid, nullable=False)
