import typing

import loguru
import sqlalchemy
from sqlalchemy import exc as sqlalchemy_error
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.profile import Profile
from src.models.schema.profile import ProfileInCreate, ProfileInResponse, ProfileInUpdate
from src.repository.crud.base import BaseCRUDRepository


class AccountCRUDRepository(BaseCRUDRepository):
    async def read_profiles(self) -> typing.Sequence[Profile]:
        stmt = sqlalchemy.select(Profile)
        query = await self.async_session.execute(statement=stmt)
        return query.scalars.all()

    async def read_profile_by_id(self, id: int) -> Profile:
        try:
            stmt = sqlalchemy.select(Profile).where(Profile.id == id)
            query = await self.async_session.execute(statement=stmt)
            return query.scalar()
        except sqlalchemy_error.DatabaseError as e:
            loguru.logger.error("Error in read_profile_by_id(): %s", e)
            raise e
