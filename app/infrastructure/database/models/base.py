import datetime as dt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from uuid import UUID, uuid4


class Base(DeclarativeBase):
    uuid: Mapped[UUID] = mapped_column(primary_key=True, index=True, default=uuid4)
    created_at: Mapped[dt.datetime] = mapped_column(default=dt.datetime.now)
    updated_at: Mapped[dt.datetime] = mapped_column(default=dt.datetime.now)


class TaskList(Base):
    __tablename__ = "tasklists"

    name: Mapped[str] = mapped_column(nullable=False)
    tasks: Mapped[list["Task"]] = relationship(
        "Task", back_populates="tasklist", cascade="all, delete"
    )


class Task(Base):
    __tablename__ = "tasks"

    name: Mapped[str] = mapped_column(nullable=False)
    completed: Mapped[bool] = mapped_column(default=False)
    tasklist_id: Mapped[UUID] = mapped_column(
        ForeignKey("tasklists.uuid"), nullable=False
    )
    tasklist: Mapped["TaskList"] = relationship("TaskList", back_populates="tasks")
