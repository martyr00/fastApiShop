from datetime import datetime

from sqlalchemy import String, Integer, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List

from .base import Base
from .product_models import Product


class Vendor(Base):
    __tablename__ = "vendor"

    name: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(13))
    email: Mapped[str] = mapped_column(String(200))
    time_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    time_updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    availability = relationship("Availability", back_populates="vendor")


class Availability(Base):
    __tablename__ = "availability"

    vendor_id: Mapped[int] = mapped_column(Integer, ForeignKey("vendor.id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"))
    vendor_price: Mapped[float] = mapped_column(Float)
    amount: Mapped[int] = mapped_column(Integer)

    vendor: Mapped[List['Vendor']] = relationship("Vendor", back_populates="availability")
    product: Mapped[List['Product']] = relationship("Product", back_populates="availability")