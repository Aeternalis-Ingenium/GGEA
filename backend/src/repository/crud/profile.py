import typing

import loguru
import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.account import Account
from src.models.db.profile import Profile
from src.models.schema.profile import ProfileInSignup, ProfileInUpdate
from src.repository.crud.base import BaseCRUDRepository
from src.utility.exceptions.custom import EntityDoesNotExist
from src.utility.exceptions.database import DatabaseError


class ProfileCRUDRepository(BaseCRUDRepository):
    async def create_profile(self, profile_create: ProfileInSignup, parent_account: Account) -> Profile:
        try:
            new_profile = Profile(
                first_name=profile_create.first_name,
                last_name=profile_create.last_name,
                photo=profile_create.photo,
                account=parent_account,
            )
            self.async_session.add(instance=new_profile)
            await self.async_session.commit()
            await self.async_session.refresh(instance=new_profile)
            return new_profile
        except DatabaseError as e:
            loguru.logger.error("Error in create_profile(): %s", e)
            # TODO: Returning custom error message to client
            raise e

    async def read_profiles(self) -> typing.Sequence[Profile]:
        stmt = sqlalchemy.select(Profile)
        query = await self.async_session.execute(statement=stmt)
        return query.scalars().all()

    async def read_profile_by_id(self, id: int) -> Profile:
        try:
            stmt = sqlalchemy.select(Profile).where(Profile.id == id)
            query = await self.async_session.execute(statement=stmt)

            if not query:
                raise EntityDoesNotExist

            return query.scalar()
        except DatabaseError as e:
            loguru.logger.error("Error in read_profile_by_id(): %s", e)
            # TODO: Returning custom error message to client
            raise e

    async def read_profile_by_first_name(self, first_name: str) -> Profile:
        try:
            stmt = sqlalchemy.select(Profile).where(Profile.first_name == first_name)
            query = await self.async_session.execute(statement=stmt)

            if not query:
                raise EntityDoesNotExist

            return query.scalar()
        except DatabaseError as e:
            loguru.logger.error("Error in read_profile_by_first_name(): %s", e)
            # TODO: Returning custom error message to client
            raise e

    async def read_profile_by_last_name(self, last_name: str) -> Profile:
        try:
            stmt = sqlalchemy.select(Profile).where(Profile.last_name == last_name)
            query = await self.async_session.execute(statement=stmt)

            if not query:
                raise EntityDoesNotExist

            return query.scalar()
        except DatabaseError as e:
            loguru.logger.error("Error in read_profile_by_last_name(): %s", e)
            # TODO: Returning custom error message to client
            raise e

    async def update_profile_by_id(self, id: int, profile_update: ProfileInUpdate) -> Profile:
        new_profile_data = profile_update.dict()
        current_profile = await self.read_profile_by_id(id)

        if not current_profile:
            raise EntityDoesNotExist(f"Profile with id '{id}' does not exist!")  # type: ignore

        update_stmt = (
            sqlalchemy.update(table=Profile)
            .where(Profile.id == current_profile.id)
            .values(updated_at=sqlalchemy_functions.now())
        )

        if new_profile_data["first_name"]:
            update_stmt = update_stmt.values(first_name=new_profile_data["first_name"])

        if new_profile_data["last_name"]:
            update_stmt = update_stmt.values(last_name=new_profile_data["last_name"])

        # if new_profile_data["photo"]:

        #     try:

        #         #TODO:  1. Getting the name # type: ignore
        #         #       2. Uploading the photo to somewhere
        #     except:

        if new_profile_data["win"]:
            update_stmt = update_stmt.values(win=new_profile_data["win"])

        if new_profile_data["loss"]:
            update_stmt = update_stmt.values(loss=new_profile_data["loss"])

        if new_profile_data["mmr"]:
            update_stmt = update_stmt.values(mmr=new_profile_data["mmr"])

        try:
            await self.async_session.execute(statement=update_stmt)
            await self.async_session.commit()
            await self.async_session.refresh(instance=current_profile)

            return current_profile

        except DatabaseError as e:
            loguru.logger.error("Error in update_profile_by_id() while trying to write changes: %s", e)
            # TODO: Returning custom error message to client
            raise e

    async def delete_profile_by_id(self, id: int) -> str:
        try:
            select_stmt = sqlalchemy.select(Profile).where(Profile.id == id)
            query = self.async_session.execute(select_stmt)
            delete_profile = query.scalar()
        except DatabaseError as e:
            loguru.logger.error("Error in delete_profile_by_id() while querying for profile: %s", e)
            # TODO: Returning custom error message to client
            raise e

        if not delete_profile:
            raise EntityDoesNotExist(f"Profile with id '{id}' does not exist!")

        try:
            delete_stmt = sqlalchemy.delete(Profile).where(Profile.id == delete_profile.id)

            await self.async_session.execute(statement=delete_stmt)
            await self.async_session.commit()

            return f"Profile with id '{id}' is successfully deleted!"

        except DatabaseError as e:
            loguru.logger.error("Error in delete_profile_by_id() while executing delete statement: %s", e)
            # TODO: Returning custom error message to client
            raise e
