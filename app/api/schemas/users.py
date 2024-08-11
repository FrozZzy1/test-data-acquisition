from pydantic import BaseModel
from datetime import datetime


class ReadUserSchema(BaseModel):
    id: int
    login: str
    is_admin: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None


class AddUserSchema(BaseModel):
    login: str
    password: str
    is_admin: bool = False


class UpdateUserSchema(BaseModel):
    login: str | None = None
    password: str | None = None
    is_admin: bool | None = None
