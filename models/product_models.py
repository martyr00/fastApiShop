from typing import List
from sqlalchemy import ForeignKey, String, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from .base import Base


class Brand(Base):
    __tablename__ = 'brand'

    title: Mapped[str] = mapped_column(String(255))

    products: Mapped[List['Product']] = relationship(back_populates='brand')


class Product(Base):
    __tablename__ = 'product'

    price_id: Mapped[int] = mapped_column(ForeignKey('product_price.id'), unique=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(1024))
    brand_id: Mapped[int] = mapped_column(ForeignKey('brand.id'))
    time_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    time_updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    brand: Mapped['Brand'] = relationship(back_populates='products')
    price: Mapped['ProductPrice'] = relationship(back_populates='product')
    images: Mapped[List['ProductImage']] = relationship(back_populates='product', cascade='all, delete-orphan')
    features: Mapped[List['ProductFeature']] = relationship(back_populates='product', cascade='all, delete-orphan')


class ProductPrice(Base):
    __tablename__ = 'product_price'

    price: Mapped[float] = mapped_column(Float)
    discount_percent: Mapped[float] = mapped_column(Float)

    product: Mapped['Product'] = relationship(back_populates='price')


class ProductImage(Base):
    __tablename__ = 'product_image'

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    url_image: Mapped[str] = mapped_column(String(255))

    product: Mapped['Product'] = relationship(back_populates='images')


class ProductFeature(Base):
    __tablename__ = 'product_features'

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    features_id: Mapped[int] = mapped_column(ForeignKey('features.id'))

    product: Mapped['Product'] = relationship(back_populates='features')
    feature: Mapped['Feature'] = relationship()


class Feature(Base):
    __tablename__ = 'features'

    key: Mapped[str] = mapped_column(String(255))
    value: Mapped[str] = mapped_column(String(255))
