import typing

import sqlalchemy
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class DBBaseTable(MappedAsDataclass, DeclarativeBase):
    metadata: sqlalchemy.MetaData = sqlalchemy.MetaData()


BaseTable: typing.Type[DeclarativeBase] = DBBaseTable
