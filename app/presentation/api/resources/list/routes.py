from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.database.models.base import TaskList as TaskListModel
from app.infrastructure.database.postgres.base import get_db
from app.presentation.api.resources.list.dtos import TaskListCreatePayload as TaskListCreatePayloadDTO
from app.presentation.api.resources.list.dtos import TaskListGetResponse as TaskListGetResponseDTO
from app.presentation.api.resources.list.dtos import TaskListCreateResponse as TaskListCreateResponseDTO

tasklist_router = APIRouter(prefix="", tags=["lists"])

@tasklist_router.get(
    "/tasklist",
    response_model=list[TaskListGetResponseDTO],
    status_code=status.HTTP_200_OK,
)
async def tasklist_all(db: Session = Depends(get_db)) -> list[TaskListGetResponseDTO]:
    return db.execute(select(TaskListModel)).scalars().all()

@tasklist_router.get(
    "/tasklist/{uuid}",
    response_model=TaskListGetResponseDTO,
    status_code=status.HTTP_200_OK,
)
async def tasklist_get(
    uuid: UUID,
    db: Session = Depends(get_db)
) -> TaskListGetResponseDTO:
    return db.execute(
        select(TaskListModel).where(TaskListModel.uuid == uuid)
    ).scalar_one()

@tasklist_router.post(
    "/tasklist",
    response_model=TaskListCreateResponseDTO,
    status_code=status.HTTP_201_CREATED,
)
async def tasklist_create(
    data: TaskListCreatePayloadDTO, db: Session = Depends(get_db)
) -> TaskListCreateResponseDTO:
    task = TaskListModel(**data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)

    return task