from uuid import UUID

from sqlalchemy import Integer, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from src.subscription.models.base import Base


class SubscriptionModel(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # noqa
    follower_id: Mapped[UUID] = mapped_column(Uuid, nullable=False)
    user_id: Mapped[UUID] = mapped_column(Uuid, nullable=False)
