from sqlalchemy import select, update, delete

from app.database.database import async_session_maker
from app.database.models.users import UserOrm


class UserRepository:
    @classmethod
    async def create_user(cls, data: dict) -> UserOrm:
        async with async_session_maker() as session:
            user = UserOrm(**data)
            session.add(user)
            await session.commit()
            await session.refresh(user)

            return user

    @classmethod
    async def get_users(cls) -> list[UserOrm]:
        async with async_session_maker() as session:
            query = select(UserOrm)
            result = await session.scalars(query)

            return result

    @classmethod
    async def update_user(cls, id: int, data: dict):
        async with async_session_maker() as session:
            query = (
                update(UserOrm)
                .filter(UserOrm.id == id)
                .values(data)
            )
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_user(cls, id: int):
        async with async_session_maker() as session:
            query = (
                delete(UserOrm)
                .filter(UserOrm.id == id)
            )
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_user_by_login(cls, login: str) -> UserOrm | None:
        async with async_session_maker() as session:
            query = (
                select(UserOrm)
                .filter(UserOrm.login == login)
            )
            result = await session.scalar(query)
            return result
