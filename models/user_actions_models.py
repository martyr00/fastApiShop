from typing import Optional
from sqlalchemy import ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from .base import Base
from .user_models import User
from .product_models import Product


class Compare(Base):
    __tablename__ = 'compare'

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), nullable=False)
    time_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    time_updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user: Mapped['User'] = relationship()
    product: Mapped['Product'] = relationship()


class Wishlist(Base):
    __tablename__ = 'wishlist'

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), nullable=False)
    time_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    time_updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user: Mapped['User'] = relationship()
    product: Mapped['Product'] = relationship()


class Card(Base):
    __tablename__ = 'card'

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    time_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    time_updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user: Mapped['User'] = relationship()
    product: Mapped['Product'] = relationship()


class Comment(Base):
    __tablename__ = 'comment'

    parent_comment_id: Mapped[Optional[int]] = mapped_column(ForeignKey('comment.id'), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), nullable=False)
    text: Mapped[str] = mapped_column(String(255), nullable=False)
    time_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    time_updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user: Mapped['User'] = relationship()
    product: Mapped['Product'] = relationship()
    parent_comment: Mapped[Optional['Comment']] = relationship(remote_side=[id])
