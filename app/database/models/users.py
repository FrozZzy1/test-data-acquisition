from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import BaseOrm


class UserOrm(BaseOrm):
    __tablename__ = 'users'

    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)
