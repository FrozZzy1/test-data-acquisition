from app.api.schemas.users import AddUserSchema, UpdateUserSchema
from app.database.models.users import UserOrm
from app.database.repositories.users import UserRepository
from app.utils.password import get_password_hash, verify_password


class UserService:
    @classmethod
    async def create_user(cls, user: AddUserSchema) -> UserOrm:
        user_dict = user.model_dump()
        user_dict['password'] = get_password_hash(user_dict['password'])
        user = await UserRepository.create_user(user_dict)
        return user

    @classmethod
    async def get_users(cls) -> list[UserOrm]:
        users = await UserRepository.get_users()
        return users

    @classmethod
    async def update_user(cls, user_id: int, user: UpdateUserSchema):
        user_dict = user.model_dump(exclude_none=True)
        if 'password' in user_dict:
            user_dict['password'] = get_password_hash(user_dict['password'])
        await UserRepository.update_user(user_id, user_dict)

    @classmethod
    async def delete_user(cls, id: int):
        await UserRepository.delete_user(id)

    @classmethod
    async def is_auth_admin(cls, login: str, password: str) -> bool:
        user = await UserRepository.get_user_by_login(login)
        return user and user.is_admin and verify_password(password, user.password) # noqa
