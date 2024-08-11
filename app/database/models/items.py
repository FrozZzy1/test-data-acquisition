from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import BaseOrm


class ItemOrm(BaseOrm):
    __tablename__ = 'items'

    name: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
    )
