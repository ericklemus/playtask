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

    async def get(self, tasklist_id: UUID, task_id: UUID) -> dict:
        return await self._get(
            model=TaskModel,
            filters={"tasklist_id": tasklist_id, "uuid": task_id},
        )

    async def create(self, tasklist_id: UUID, data: dict) -> dict:
        return await self._create(
            model=TaskModel,
            data={"tasklist_id": tasklist_id, **data},
        )

    async def update(self, tasklist_id: UUID, task_id: UUID, data: dict) -> dict:
        return await self._update(
            model=TaskModel,
            data=data,
            filters={"tasklist_id": tasklist_id, "uuid": task_id},
        )

    async def delete(self, tasklist_id: UUID, task_id: UUID) -> None:
        return await self._delete(
            model=TaskModel,
            filters={"tasklist_id": tasklist_id, "uuid": task_id},
        )
