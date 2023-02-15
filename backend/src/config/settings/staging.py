import decouple

from src.config.settings.base import Settings
from src.config.settings.environment import Environment


class StagingSettings(Settings):
    DESCRIPTION: str | None = (
        "Test Settings -- Backend application with FastAPI, PostgreSQL via SQLAlchemy with Alembic, and Docker."
    )
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.STAGING
    DB_POSTGRES_NAME: str = decouple.config("POSTGRES_TEST_DB", cast=str)  # type: ignore
    DB_POSTGRES_HOST: str = decouple.config("POSTGRES_TEST_HOST", cast=str)  # type: ignore
