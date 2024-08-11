from pydantic import BaseModel
from datetime import datetime


class ReadItemSchema(BaseModel):
    id: int
    name: str
    user_id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None


class AddItemSchema(BaseModel):
    name: str
    user_id: int


class UpdateItemSchema(BaseModel):
    name: str | None = None
    user_id: int | None = None
