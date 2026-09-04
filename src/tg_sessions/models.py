from datetime import datetime
from typing import Optional

from sqlalchemy import Text, DateTime, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, uuid_pk, uuid_fk


class TgSessions(Base):
    __tablename__ = "tg_sessions"

    session_uuid: Mapped[uuid_pk]
    tg_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    user_uuid: Mapped[uuid_fk] = mapped_column(nullable=True)
    state: Mapped[str] = mapped_column(Text)
    context: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True),
                                                           server_default=func.now(),
                                                           nullable=True)


