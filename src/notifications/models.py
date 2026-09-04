import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, Enum, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, uuid_pk, uuid_fk

class NotificationType(enum.Enum):
    email = "email"
    telegram = "telegram"

class NotificationStatus(enum.Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"


class Notifications(Base):
    __tablename__ = "notifications"

    notification_uuid: Mapped[uuid_pk]
    user_uuid: Mapped[uuid_fk] = mapped_column(ForeignKey("users.user_uuid"))
    type: Mapped[NotificationType] = mapped_column(
        Enum(NotificationType),
        nullable=False,
    )
    subject: Mapped[str] = mapped_column(nullable=True)
    body: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[NotificationStatus] = mapped_column(Enum(NotificationStatus))
    sent_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
