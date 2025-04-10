from uuid import UUID

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from sqlalchemy import Uuid

class User(Base):
    __tablename__ = "users"

    user_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
