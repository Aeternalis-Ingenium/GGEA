import fastapi
import loguru
from sqlalchemy import event
from sqlalchemy.dialects.postgresql.asyncpg import AsyncAdapt_asyncpg_connection as AsyncPGConnection
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.pool.base import _ConnectionRecord as ConnectionRecord

from src.repository.base import BaseTable
from src.repository.database import db


@event.listens_for(target=db.async_engine.sync_engine, identifier="connect")
def inspect_db_server_on_connection(db_api_connection: AsyncPGConnection, connection_record: ConnectionRecord) -> None:
    loguru.logger.info(f"New DB API Connection ---\n {db_api_connection}")
    loguru.logger.info(f"Connection Record ---\n {connection_record}")


@event.listens_for(target=db.async_engine.sync_engine, identifier="close")
def inspect_db_server_on_close(db_api_connection: AsyncPGConnection, connection_record: ConnectionRecord) -> None:
    loguru.logger.info(f"Closing DB API Connection ---\n {db_api_connection}")
    loguru.logger.info(f"Closed Connection Record ---\n {connection_record}")


async def initialize_db_tables(connection: AsyncConnection) -> None:
    loguru.logger.info("Database Table Creation --- Initializing . . .")

    await connection.run_sync(BaseTable.metadata.drop_all)  # type: ignore
    await connection.run_sync(BaseTable.metadata.create_all)  # type: ignore

    loguru.logger.info("Database Table Creation --- Successfully Initialized!")


async def initialize_db_connection(app: fastapi.FastAPI) -> None:
    loguru.logger.info("Database Connection --- Establishing . . .")

    app.state.db = db

    async with app.state.db.async_engine.begin() as connection:
        await initialize_db_tables(connection=connection)

    loguru.logger.info("Database Connection --- Successfully Established!")


async def dispose_db_connection(app: fastapi.FastAPI) -> None:
    loguru.logger.info("Database Connection --- Disposing . . .")

    await app.state.db.async_engine.dispose()

    loguru.logger.info("Database Connection --- Successfully Disposed!")
