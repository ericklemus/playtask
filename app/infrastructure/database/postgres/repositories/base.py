from typing import TypeVar
from sqlalchemy import select, update, delete, and_
from sqlalchemy.orm import Session

TBase = TypeVar("Base")


class Base:
    def __init__(self, session: Session) -> TBase:
        self._session = session

    def _get_filters_parsed(self, model: TBase, filters: dict) -> dict:
        return (getattr(model, key) == value for key, value in filters.items())

    async def _all(self, model: TBase, filters: dict = None) -> TBase:
        try:
            filters_parsed = self._get_filters_parsed(model, filters) if filters else {}
            query = (
                select(model)
                .where(and_(True, *filters_parsed))
                .order_by(model.created_at.desc())
            )
            return self._session.execute(query).scalars().all()
        except Exception as e:
            await self._session.rollback()
            raise e

    async def _get(self, model: TBase, filters: dict) -> TBase:
        try:
            filters_parsed = self._get_filters_parsed(model, filters)
            query = select(model).where(and_(True, *filters_parsed))
            return self._session.execute(query).scalar_one()
        except Exception as e:
            self._session.rollback()
            raise e

    async def _create(self, model: TBase, data: dict) -> TBase:
        try:
            instance = model(**data)
            self._session.add(instance)
            await self._session.commit()
            await self._session.refresh(instance)
        except Exception as e:
            self._session.rollback()
            raise e

    async def _update(self, model: TBase, data: dict, filters: dict) -> TBase:
        try:
            filters_parsed = self._get_filters_parsed(model, filters)
            query = update(model).where(and_(True, *filters_parsed)).values(**data)
            await self._session.execute(query)
            await self._session.commit()
            instance = await self._get(model, filters)
            return instance
        except Exception as e:
            self._session.rollback()
            raise e

    async def _delete(self, model: TBase, filters: dict) -> TBase:
        try:
            filters_parsed = self._get_filters_parsed(model, filters)
            query = delete(model).where(and_(*filters_parsed))
            await self._session.execute(query)
            await self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e
