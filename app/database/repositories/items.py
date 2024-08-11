from sqlalchemy import select, update, delete

from app.database.database import async_session_maker
from app.database.models.items import ItemOrm


class ItemRepository:
    @classmethod
    async def create_item(cls, data: dict) -> ItemOrm:
        async with async_session_maker() as session:
            item = ItemOrm(**data)
            session.add(item)
            await session.commit()
            await session.refresh(item)
            return item

    @classmethod
    async def get_items(cls):
        async with async_session_maker() as session:
            query = (
                select(ItemOrm)
            )
            result = await session.execute(query)
            return result.scalars()

    @classmethod
    async def update_item(cls, id: int, data: dict):
        async with async_session_maker() as session:
            query = (
                update(ItemOrm)
                .filter(ItemOrm.id == id)
                .values(data)
            )
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_item(cls, id: int):
        async with async_session_maker() as session:
            query = (
                delete(ItemOrm)
                .filter(ItemOrm.id == id)
            )
            await session.execute(query)
            await session.commit()
