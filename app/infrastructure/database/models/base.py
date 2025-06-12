import datetime as dt

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid import UUID, uuid4


class Base(DeclarativeBase):
    uuid: Mapped[UUID] = mapped_column(primary_key=True, index=True, default=uuid4)
    created_at: Mapped[dt.datetime] = mapped_column(default=dt.datetime.now)
    updated_at: Mapped[dt.datetime] = mapped_column(default=dt.datetime.now)


class Task(Base):
    __tablename__ = "tasks"

    name: Mapped[str] = mapped_column(nullable=False)
