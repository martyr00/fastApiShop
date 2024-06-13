from sqlalchemy import Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from .base import Base
from .product_models import Product
from .user_models import User


class Views(Base):
    __tablename__ = 'views'

    product_id: Mapped[int] = mapped_column(Integer, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    time_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    product: Mapped['Product'] = relationship()
    user: Mapped['User'] = relationship()
