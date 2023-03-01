import datetime

import pydantic
import sqlalchemy
from sqlalchemy.orm import (
    Mapped as SQLAlchemyMapped,
    mapped_column as sqlalchemy_mapped_column,
    relationship as sqlalchemy_relationship,
)
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.base import DBBaseTable
from src.security.authentication.password import pwd_manager


class Account(DBBaseTable):
    __tablename__ = "account"

    id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True, autoincrement="auto")
    username: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(
        sqlalchemy.String(length=64), nullable=False, unique=True
    )
    email: SQLAlchemyMapped[pydantic.EmailStr] = sqlalchemy_mapped_column(
        sqlalchemy.String(length=64), nullable=False, unique=True
    )
    _hashed_password: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=1024), nullable=False)
    _hashed_salt: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=1024), nullable=False)
    is_admin: SQLAlchemyMapped[bool] = sqlalchemy_mapped_column(sqlalchemy.Boolean, default=False)
    is_logged_in: SQLAlchemyMapped[bool] = sqlalchemy_mapped_column(sqlalchemy.Boolean, default=True)
    is_verified: SQLAlchemyMapped[bool] = sqlalchemy_mapped_column(sqlalchemy.Boolean, default=False)
    created_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True), nullable=False, server_default=sqlalchemy_functions.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=True,
        server_onupdate=sqlalchemy.schema.FetchedValue(for_update=True),
    )
    profile = sqlalchemy_relationship("Profile", uselist=False, back_populates="account")

    __mapper_args__ = {"eager_defaults": True}

    @property
    def hashed_password(self) -> str:
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, password: str) -> None:
        self._hashed_password = password

    @property
    def hashed_salt(self) -> str:
        return self._hashed_salt

    @hashed_salt.setter
    def hashed_salt(self, salt: str) -> None:
        self._hashed_salt = salt

    def set_password(self, password: str) -> tuple[str, str]:
        return pwd_manager.generate_double_layered_password(password=password)

    def is_password_verified(self, password: str) -> bool:
        return pwd_manager.is_hashed_password_verified(hashed_salt=self.hashed_salt, password=password, hashed_password=self.hashed_password)  # type: ignore
