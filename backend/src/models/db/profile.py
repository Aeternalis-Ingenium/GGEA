import datetime

import sqlalchemy
from sqlalchemy.orm import (
    Mapped as SQLAlchemyMapped,
    mapped_column as sqlalchemy_mapped_column,
    relationship as sqlalchemy_relationship,
)
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.base import DBBaseTable


class Profile(DBBaseTable):
    __tablename__ = "profile"

    id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True, autoincrement="auto")
    first_name: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=64), nullable=True)
    last_name: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=64), nullable=True)
    photo: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=248), nullable=True)
    win: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.Integer(), nullable=False, default=0)
    loss: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.Integer(), nullable=False, default=0)
    mmr: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.Integer(), nullable=False, default=80)
    created_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True), nullable=False, server_default=sqlalchemy_functions.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=True,
        server_onupdate=sqlalchemy.schema.FetchedValue(for_update=True),
        default=None,
    )
    account_id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("account.id"), unique=True)
    account = sqlalchemy_relationship("Account", back_populates="profile")
