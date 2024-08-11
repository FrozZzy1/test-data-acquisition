from typing import Annotated
from fastapi import APIRouter, Depends, status
from app.api.dependencies.auth import get_current_login

from app.api.schemas.items import AddItemSchema, ReadItemSchema, UpdateItemSchema # noqa
from app.services.items import ItemService


items_router = APIRouter(
    prefix='/items',
    tags=['Items'],
)


@items_router.post(
    '',
    response_model=ReadItemSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    login: Annotated[str, Depends(get_current_login)],
    item: AddItemSchema,
):
    item = await ItemService.create_item(item)
    return item


@items_router.get(
    '',
    response_model=list[ReadItemSchema],
    status_code=status.HTTP_200_OK,
)
async def get_all(
    login: Annotated[str, Depends(get_current_login)],
):
    items = await ItemService.get_items()
    return items


@items_router.patch(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update(
    login: Annotated[str, Depends(get_current_login)],
    id: int,
    item: UpdateItemSchema,
):
    await ItemService.update_item(id, item)


@items_router.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    login: Annotated[str, Depends(get_current_login)],
    id: int
):
    await ItemService.delete_item(id)
