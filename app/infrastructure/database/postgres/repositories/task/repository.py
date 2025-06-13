from uuid import UUID

from app.infrastructure.database.models.base import Task as TaskModel
from app.infrastructure.database.postgres.repositories.base import (
    Base as BaseRepository,
)
from app.domain.task.repository import Task as TaskRepository


class Task(BaseRepository, TaskRepository):
    async def all(self, filters: dict) -> list[dict]:
        return await self._all(
            model=TaskModel,
            filters=filters,
        )

    async def get(self, uuid: UUID) -> dict:
        return await self._get(
            model=TaskModel,
            filters={"uuid": uuid},
        )

    async def create(self, data: dict) -> dict:
        return await self._get(
            model=TaskModel,
            data=data,
        )

    async def update(self, uuid: UUID, data: dict) -> dict:
        return await self._update(
            model=TaskModel,
            data=data,
            filters={"uuid": uuid},
        )

    async def delete(self, uuid: UUID) -> None:
        return await self._delete(
            model=TaskModel,
            filters={"uuid": uuid},
        )
