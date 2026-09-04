from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, uuid_pk


class PipelineStages(Base):
    stage_uuid: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(nullable=False)
    order: Mapped[int] = mapped_column(nullable=False)
    is_final: Mapped[bool]