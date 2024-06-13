from typing import List
from sqlalchemy import ForeignKey, String, Integer, Enum as SQLAlchemyEnum, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from enum import Enum

from .base import Base


class RoleEnum(str, Enum):
    GUEST = "GUEST"
    USER = "USER"
    ADMIN = "ADMIN"
    SUPER_ADMIN = "SUPER_ADMIN"


class User(Base):
    __tablename__ = 'user'

    URL_image: Mapped[str] = mapped_column(String(255), nullable=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=True)
    second_name: Mapped[str] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str] = mapped_column(String(255), nullable=True)
    email: Mapped[str] = mapped_column(String(255), nullable=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    password: Mapped[str] = mapped_column(String(255), nullable=True)
    role: Mapped[RoleEnum] = mapped_column(SQLAlchemyEnum(RoleEnum), nullable=False)
    uuid: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    time_updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    time_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    settings: Mapped[List['UserSettings']] = relationship(back_populates='user', cascade='all, delete-orphan')


class UserSettings(Base):
    __tablename__ = 'user_settings'

    theme: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    user: Mapped['User'] = relationship(back_populates='settings')
