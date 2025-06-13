from uuid import UUID

from app.infrastructure.database.models.base import TaskList as TaskListModel
from app.infrastructure.database.postgres.repositories.base import (
    Base as BaseRepository,
)
from app.domain.list.repository import TaskList as TaskListRepository


class TaskList(BaseRepository, TaskListRepository):
    async def all(self, filters: dict) -> list[dict]:
        return await self._all(
            model=TaskListModel,
            filters=filters,
        )

    async def get(self, uuid: UUID) -> dict:
        return await self._get(
            model=TaskListModel,
            filters={"uuid": uuid},
        )

    async def create(self, data: dict) -> dict:
        return await self._get(
            model=TaskListModel,
            data=data,
        )

    async def update(self, uuid: UUID, data: dict) -> dict:
        return await self._update(
            model=TaskListModel,
            data=data,
            filters={"uuid": uuid},
        )

    async def delete(self, uuid: UUID) -> None:
        return await self._delete(
            model=TaskListModel,
            filters={"uuid": uuid},
        )
