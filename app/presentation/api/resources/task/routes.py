from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.database.models.base import Task as TaskModel
from app.infrastructure.database.postgres.base import get_db
from app.presentation.api.resources.task.dtos import (
    TaskCreatePayload as TaskCreatePayloadDTO,
)
from app.presentation.api.resources.task.dtos import (
    TaskGetResponse as TaskGetResponseDTO,
)
from app.presentation.api.resources.task.dtos import (
    TaskCreateResponse as TaskCreateResponseDTO,
)

task_router = APIRouter(prefix="", tags=["tasks"])


@task_router.get(
    "/task",
    response_model=list[TaskGetResponseDTO],
    status_code=status.HTTP_200_OK,
)
async def task_all(db: Session = Depends(get_db)) -> list[TaskGetResponseDTO]:
    return db.execute(select(TaskModel)).scalars().all()


@task_router.get(
    "/task/{uuid}",
    response_model=TaskGetResponseDTO,
    status_code=status.HTTP_200_OK,
)
async def task_get(uuid: UUID, db: Session = Depends(get_db)) -> TaskGetResponseDTO:
    return db.execute(select(TaskModel).where(TaskModel.uuid == uuid)).scalar_one()


@task_router.post(
    "/task",
    response_model=TaskCreateResponseDTO,
    status_code=status.HTTP_201_CREATED,
)
async def task_create(
    data: TaskCreatePayloadDTO, db: Session = Depends(get_db)
) -> TaskCreateResponseDTO:
    task = TaskModel(**data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)

    return task
