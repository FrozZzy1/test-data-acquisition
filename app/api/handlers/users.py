from typing import Annotated
from fastapi import APIRouter, Depends, status

from app.api.dependencies.auth import get_current_login
from app.api.schemas.users import AddUserSchema, ReadUserSchema, UpdateUserSchema # noqa
from app.services.users import UserService

users_router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@users_router.post(
    '',
    response_model=ReadUserSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    login: Annotated[str, Depends(get_current_login)],
    user: AddUserSchema,
):
    user = await UserService.create_user(user)
    return user


@users_router.get('', response_model=list[ReadUserSchema])
async def get_all(
    login: Annotated[str, Depends(get_current_login)],
):
    users = await UserService.get_users()
    return users


@users_router.patch(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update(
    login: Annotated[str, Depends(get_current_login)],
    id: int,
    user: UpdateUserSchema,
):
    await UserService.update_user(id, user)


@users_router.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    login: Annotated[str, Depends(get_current_login)],
    id: int,
):
    await UserService.delete_user(id)
