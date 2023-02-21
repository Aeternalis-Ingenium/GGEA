import typing

import sqlalchemy
from sqlalchemy.orm import DeclarativeBase


class DBBaseTable(DeclarativeBase):
    metadata: sqlalchemy.MetaData = sqlalchemy.MetaData()


BaseTable: typing.Type[DeclarativeBase] = DBBaseTable
