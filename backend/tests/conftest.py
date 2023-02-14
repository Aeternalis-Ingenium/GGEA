import asgi_lifespan
import fastapi
import httpx
import pytest

from src.main import initialize_application


@pytest.fixture(name="test_app")
def test_app() -> fastapi.FastAPI:
    """
    A fixture to initialize FastAPI instance as test application.
    """

    return initialize_application()


@pytest.fixture(name="initialize_test_application")
async def initialize_test_application(test_app: fastapi.FastAPI) -> fastapi.FastAPI:  # type: ignore
    async with asgi_lifespan.LifespanManager(test_app):
        yield test_app


@pytest.fixture(name="async_client")
async def async_client(initialize_test_application: fastapi.FastAPI) -> httpx.AsyncClient:  # type: ignore
    async with httpx.AsyncClient(
        app=initialize_test_application,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client
