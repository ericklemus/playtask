from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid import UUID, uuid4


class Base(DeclarativeBase):
    pass 


class Task(Base):
    __tablename__ = 'tasks'

    uuid: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    name: Mapped[str] = mapped_column(nullable=False)