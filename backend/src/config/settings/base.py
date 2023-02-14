import logging
import pathlib

import decouple
import pydantic

ROOT_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent.parent.resolve()


class Settings(pydantic.BaseSettings):
    TITLE: str = "Gotta Guess'Em All!"
    VERSION: str = "0.1.0"
    TIMEZONE: str = "UTC"
    DESCRIPTION: str | None = None
    DEBUG: bool = False

    SERVER_HOST: str = decouple.config("BACKEND_SERVER_HOST", cast=str)  # type: ignore
    SERVER_PORT: int = decouple.config("BACKEND_SERVER_PORT", cast=int)  # type: ignore
    SERVER_WORKERS: int = decouple.config("BACKEND_SERVER_WORKERS", cast=int)  # type: ignore
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""

    DB_POSTGRES_HOST: str = decouple.config("POSTGRES_HOST", cast=str)  # type: ignore
    DB_MAX_POOL_CON: int = decouple.config("DB_MAX_POOL_CON", cast=int)  # type: ignore
    DB_POSTGRES_NAME: str = decouple.config("POSTGRES_DB", cast=str)  # type: ignore
    DB_POSTGRES_PASSWORD: str = decouple.config("POSTGRES_PASSWORD", cast=str)  # type: ignore
    DB_POOL_SIZE: int = decouple.config("DB_POOL_SIZE", cast=int)  # type: ignore
    DB_POOL_OVERFLOW: int = decouple.config("DB_POOL_OVERFLOW", cast=int)  # type: ignore
    DB_POSTGRES_PORT: int = decouple.config("POSTGRES_PORT", cast=int)  # type: ignore
    DB_POSTGRES_SCHEMA: str = decouple.config("POSTGRES_SCHEMA", cast=str)  # type: ignore
    DB_TIMEOUT: int = decouple.config("DB_TIMEOUT", cast=int)  # type: ignore
    DB_POSTGRES_USENRAME: str = decouple.config("POSTGRES_USERNAME", cast=str)  # type: ignore

    IS_DB_ECHO_LOG: bool = decouple.config("IS_DB_ECHO_LOG", cast=bool)  # type: ignore
    IS_DB_FORCE_ROLLBACK: bool = decouple.config("IS_DB_FORCE_ROLLBACK", cast=bool)  # type: ignore
    IS_DB_EXPIRE_ON_COMMIT: bool = decouple.config("IS_DB_EXPIRE_ON_COMMIT", cast=bool)  # type: ignore

    API_TOKEN: str = decouple.config("API_TOKEN", cast=str)  # type: ignore
    AUTH_TOKEN: str = decouple.config("AUTH_TOKEN", cast=str)  # type: ignore
    JWT_TOKEN_PREFIX: str = decouple.config("JWT_TOKEN_PREFIX", cast=str)  # type: ignore
    JWT_SECRET_KEY: str = decouple.config("JWT_SECRET_KEY", cast=str)  # type: ignore
    JWT_SUBJECT: str = decouple.config("JWT_SUBJECT", cast=str)  # type: ignore
    JWT_MIN: int = decouple.config("JWT_MIN", cast=int)  # type: ignore
    JWT_HOUR: int = decouple.config("JWT_HOUR", cast=int)  # type: ignore
    JWT_DAY: int = decouple.config("JWT_DAY", cast=int)  # type: ignore
    JWT_ACCESS_TOKEN_EXPIRATION_TIME: int = JWT_MIN * JWT_HOUR * JWT_DAY

    IS_ALLOWED_CREDENTIALS: bool = decouple.config("IS_ALLOWED_CREDENTIALS", cast=bool)  # type: ignore
    ALLOWED_ORIGINS: list[str] = [
        decouple.config("ALLOWED_ORIGIN_FRONTEND_LOCALHOST_DEFAULT", cast=str),  # type: ignore
        decouple.config("ALLOWED_ORIGIN_FRONTEND_LOCALHOST_CUSTOM", cast=str),  # type: ignore
        decouple.config("ALLOWED_ORIGIN_FRONTEND_DOCKER", cast=str),  # type: ignore
        decouple.config("ALLOWED_ORIGIN_FRONTEND_PRODUCTION", cast=str),  # type: ignore
    ]
    ALLOWED_METHODS: list[str] = [decouple.config("ALLOWED_METHOD_1")]  # type: ignore
    ALLOWED_HEADERS: list[str] = [decouple.config("ALLOWED_HEADER_1")]  # type: ignore

    LOGGING_LEVEL: int = logging.INFO
    LOGGERS: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    BCRYPT_HASHING_ALGORITHM: str = decouple.config("BCRYPT_HASHING_ALGORITHM", cast=str)  # type: ignore
    ARGON2_HASHING_ALGORITHM: str = decouple.config("ARGON2_HASHING_ALGORITHM", cast=str)  # type: ignore
    SHA256_HASHING_ALGORITHM: str = decouple.config("SHA256_HASHING_ALGORITHM", cast=str)  # type: ignore
    SHA512_HASHING_ALGORITHM: str = decouple.config("SHA512_HASHING_ALGORITHM", cast=str)  # type: ignore
    HASHING_SALT: str = decouple.config("HASHING_SALT", cast=str)  # type: ignore
    PWD_ALGORITHM_LAYER_1: str = decouple.config("PWD_ALGORITHM_LAYER_1", cast=str)  # type: ignore
    PWD_ALGORITHM_LAYER_2: str = decouple.config("PWD_ALGORITHM_LAYER_2", cast=str)  # type: ignore
    JWT_ALGORITHM: str = decouple.config("JWT_ALGORITHM", cast=str)  # type: ignore

    AWS_S3_BUCKET: str = decouple.config("AWS_S3_BUCKET", cast=str)  # type: ignore
    AWS_S3_BUCKET_ARN: str = decouple.config("AWS_S3_BUCKET_ARN", cast=str)  # type: ignore
    AWS_S3_POKEMON_IMAGE_URI: str = decouple.config("AWS_S3_POKEMON_IMAGE_URI", cast=str)  # type: ignore
    AWS_S3_SKLEARN_MODEL_URI: str = decouple.config("AWS_S3_SKLEARN_MODEL_URI", cast=str)  # type: ignore
    AWS_S3_TF_MODEL_URI: str = decouple.config("AWS_S3_TF_MODEL_URI", cast=str)  # type: ignore
    AWS_IAM_USERNAME: str = decouple.config("AWS_IAM_USERNAME", cast=str)  # type: ignore
    AWS_IAM_ARN: str = decouple.config("AWS_IAM_ARN", cast=str)  # type: ignore
    AWS_SERVICE_NAME: str = decouple.config("AWS_SERVICE_NAME", cast=str)  # type: ignore
    AWS_SERVICE_REGION: str = decouple.config("AWS_SERVICE_REGION", cast=str)  # type: ignore
    AWS_ACCESS_KEY: str = decouple.config("AWS_ACCESS_KEY", cast=str)  # type: ignore
    AWS_SECRET_ACCESS_KEY: str = decouple.config("AWS_SECRET_ACCESS_KEY", cast=str)  # type: ignore
    AWS_S3_POKEMON_IMAGE_DIR: str = decouple.config("AWS_S3_POKEMON_IMAGE_DIR", cast=str)  # type: ignore
    AWS_S3_SKLEARN_MODEL_DIR: str = decouple.config("AWS_S3_SKLEARN_MODEL_DIR", cast=str)  # type: ignore
    AWS_S3_TF_MODEL_DIR: str = decouple.config("AWS_S3_TF_MODEL_DIR", cast=str)  # type: ignore

    TF_MODEL_FILE_EXTENSION: str = decouple.config("TF_MODEL_FILE_EXTENSION", cast=str)  # type: ignore
    SKLEARN_MODEL_FILE_EXTENSION: str = decouple.config("SKLEARN_MODEL_FILE_EXTENSION", cast=str)  # type: ignore
    PYTORCH_MODEL_FILE_EXTENSION: str = decouple.config("PYTORCH_MODEL_FILE_EXTENSION", cast=str)  # type: ignore

    class Config(pydantic.BaseConfig):
        case_sensitive: bool = True
        env_file: str = f"{str(ROOT_DIR)}/.env"
        validate_assignment: bool = True

    @property
    def set_backend_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` instance attributes with the custom values defined in `Settings`.
        """
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }
