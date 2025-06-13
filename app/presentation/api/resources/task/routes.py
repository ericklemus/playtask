from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.database.models.base import Task as TaskModel
from app.infrastructure.database.postgres.base import get_db
from app.presentation.api.resources.task.dtos import (
    TaskGetResponse as TaskGetResponseDTO,
    TaskAllBaseResponse as TaskAllBaseResponseDTO,
    TaskAllResponse as TaskAllResponseDTO,
    TaskCreatePayload as TaskCreatePayloadDTO,
    TaskCreateResponse as TaskCreateResponseDTO,
    TaskUpdatePayload as TaskUpdatePayloadDTO,
    TaskUpdateResponse as TaskUpdateResponseDTO,
    TaskDeleteResponse as TaskDeleteResponseDTO,
)

task_router = APIRouter(prefix="", tags=["tasks"])


@task_router.get(
    "/tasklist/{tasklist_id}/task",
    response_model=TaskAllResponseDTO,
    status_code=status.HTTP_200_OK,
)
async def task_all(
    tasklist_id: UUID,
    db: Session = Depends(get_db),
) -> TaskAllResponseDTO:
    tasks = (
        db.execute(select(TaskModel).where(TaskModel.tasklist_id == tasklist_id))
        .scalars()
        .all()
    )

    total = len(tasks)
    completed_percentage = (
        sum(1 for task in tasks if task.completed) / total if total else 0.0
    )

    dto_tasks = [TaskAllBaseResponseDTO.from_orm(task) for task in tasks]

    return TaskAllResponseDTO(
        tasks=dto_tasks,
        completed_percentage=completed_percentage,
    )


@task_router.get(
    "/tasklist/{tasklist_id}/task/{task_id}",
    response_model=TaskGetResponseDTO,
    status_code=status.HTTP_200_OK,
)
async def task_get(
    tasklist_id: UUID,
    task_id: UUID,
    db: Session = Depends(get_db),
) -> TaskGetResponseDTO:
    task = db.execute(
        select(TaskModel).where(
            (TaskModel.tasklist_id == tasklist_id) & (TaskModel.uuid == task_id)
        )
    ).scalar_one_or_none()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@task_router.post(
    "/tasklist/{tasklist_id}/task",
    response_model=TaskCreateResponseDTO,
    status_code=status.HTTP_201_CREATED,
)
async def task_create(
    tasklist_id: UUID,
    data: TaskCreatePayloadDTO,
    db: Session = Depends(get_db),
) -> TaskCreateResponseDTO:
    task_data = data.model_dump()
    task_data["tasklist_id"] = tasklist_id
    task = TaskModel(**task_data)
    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@task_router.put(
    "/tasklist/{tasklist_id}/task/{task_id}",
    response_model=TaskUpdateResponseDTO,
    status_code=status.HTTP_201_CREATED,
)
async def task_update(
    tasklist_id: UUID,
    task_id: UUID,
    data: TaskUpdatePayloadDTO,
    db: Session = Depends(get_db),
) -> TaskUpdateResponseDTO:
    task = db.execute(
        select(TaskModel).where(
            (TaskModel.tasklist_id == tasklist_id) & (TaskModel.uuid == task_id)
        )
    ).scalar_one_or_none()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(task, key, value)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@task_router.delete(
    "/tasklist/{tasklist_id}/task/{task_id}",
    response_model=TaskDeleteResponseDTO,
    status_code=status.HTTP_200_OK,
)
async def task_delete(
    tasklist_id: UUID,
    task_id: UUID,
    db: Session = Depends(get_db),
) -> TaskDeleteResponseDTO:
    task = db.execute(
        select(TaskModel).where(
            (TaskModel.tasklist_id == tasklist_id) & (TaskModel.uuid == task_id)
        )
    ).scalar_one_or_none()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"msg": "Task deleted"}


@task_router.patch(
    "/tasklist/{tasklist_id}/task/{task_id}/toggle",
    response_model=TaskGetResponseDTO,
    status_code=status.HTTP_200_OK,
)
async def task_toggle_completed(
    tasklist_id: UUID,
    task_id: UUID,
    db: Session = Depends(get_db),
):
    task = db.execute(
        select(TaskModel).where(
            (TaskModel.tasklist_id == tasklist_id) & (TaskModel.uuid == task_id)
        )
    ).scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.completed = not task.completed

    db.commit()
    db.refresh(task)

    return task
