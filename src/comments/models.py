from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database import uuid_pk, Base, uuid_fk


class Comments(Base):
    __tablename__ = "comments"

    comment_uuid: Mapped[uuid_pk]
    body: Mapped[str] = mapped_column(nullable=False)
    contact_uuid: Mapped[Optional[uuid_fk]] = mapped_column(ForeignKey("contacts.contact_uuid"), nullable=True)
    deal_uuid: Mapped[Optional[uuid_fk]] = mapped_column(ForeignKey("deals.deal_uuid"), nullable=True)
    author: Mapped[Optional[uuid_fk]] = mapped_column(ForeignKey("users.user_uuid"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())