from typing import List
from sqlalchemy import ForeignKey, String, Integer, Enum as SQLAlchemyEnum, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from enum import Enum

from .base import Base
from .product_models import Product
from .user_models import User


class PaymentTypeEnum(str, Enum):
    CARD = "CARD"
    CASH = "CASH"
    APPLE_PAY = "APPLE_PAY"
    GOOGLE_PAY = "GOOGLE_PAY"


class DeliveryTypeEnum(str, Enum):
    NOVA_POSHTA = "NOVA_POSHTA"
    COURIER = "COURIER"


class OrderStatusEnum(str, Enum):
    PENDING = "PENDING"
    NEEDS_TO_SEND = "NEEDS_TO_SEND"
    SEND = "SEND"
    DONE = "DONE"
    CANCELED = "CANCELED"


class PaymentType(Base):
    __tablename__ = 'payment_type'

    type: Mapped[PaymentTypeEnum] = mapped_column(SQLAlchemyEnum(PaymentTypeEnum), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)


class DeliveryType(Base):
    __tablename__ = 'delivery_type'

    type: Mapped[DeliveryTypeEnum] = mapped_column(SQLAlchemyEnum(DeliveryTypeEnum), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)


class City(Base):
    __tablename__ = 'city'

    name: Mapped[str] = mapped_column(String(255), nullable=False)


class Order(Base):
    __tablename__ = 'order'

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    city_id: Mapped[int] = mapped_column(ForeignKey('city.id'), nullable=False)
    delivery_type_id: Mapped[int] = mapped_column(ForeignKey('delivery_type.id'), nullable=False)
    payment_type_id: Mapped[int] = mapped_column(ForeignKey('payment_type.id'), nullable=False)
    status: Mapped[OrderStatusEnum] = mapped_column(SQLAlchemyEnum(OrderStatusEnum), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=True)
    delivery_service_id: Mapped[int] = mapped_column(Integer, nullable=True)
    time_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    time_updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user: Mapped['User'] = relationship()
    city: Mapped['City'] = relationship()
    delivery_type: Mapped['DeliveryType'] = relationship()
    payment_type: Mapped['PaymentType'] = relationship()
    order_products: Mapped[List['OrderProducts']] = relationship(back_populates='order', cascade='all, delete-orphan')


class OrderProducts(Base):
    __tablename__ = 'order_products'

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), nullable=False )
    order_id: Mapped[int] = mapped_column(ForeignKey('order.id'), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)

    order: Mapped['Order'] = relationship(back_populates='order_products')
    product: Mapped['Product'] = relationship(back_populates='products')
