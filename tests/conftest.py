import pytest
from httpx import AsyncClient

from app.main import app


@pytest.fixture(scope="module")
async def async_client() -> AsyncClient:
    """
    Testler için asenkron bir HTTP istemcisi oluşturur.
    'async with' bloğu sayesinde testler bittiğinde istemci temizlenir.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client