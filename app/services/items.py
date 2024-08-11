from app.api.schemas.items import AddItemSchema, UpdateItemSchema
from app.database.models.items import ItemOrm
from app.database.repositories.items import ItemRepository


class ItemService:
    @classmethod
    async def create_item(cls, item: AddItemSchema) -> ItemOrm:
        item_dict = item.model_dump()
        item = await ItemRepository.create_item(item_dict)
        return item

    @classmethod
    async def get_items(cls) -> list[ItemOrm]:
        items = await ItemRepository.get_items()
        return items

    @classmethod
    async def update_item(cls, item_id: int, item: UpdateItemSchema):
        item_dict = item.model_dump()
        data = {key: value for key, value in item_dict.items() if value}
        await ItemRepository.update_item(item_id, data)

    @classmethod
    async def delete_item(cls, id: int):
        await ItemRepository.delete_item(id)
