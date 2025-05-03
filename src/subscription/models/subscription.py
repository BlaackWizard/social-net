from uuid import UUID

from sqlalchemy import Integer, Uuid
from sqlalchemy.orm import mapped_column, Mapped

from src.subscription.models.base import Base


class SubscriptionModel(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    follower_id: Mapped[UUID] = mapped_column(Uuid, nullable=False)
    user_id: Mapped[UUID] = mapped_column(Uuid, nullable=False)
