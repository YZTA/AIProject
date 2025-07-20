import pytest
from httpx import AsyncClient

# pytest'in asenkron testleri çalıştırabilmesi için bu işaretleyici gerekli
pytestmark = pytest.mark.asyncio


class TestRoot:
    async def test_read_root(self, async_client: AsyncClient):
        """
        Kök endpoint'in (/) 200 OK durum kodu ve doğru mesajı döndürdüğünü test eder.
        """
        # GIVEN: Test istemcisi (fixture'dan gelir)

        # WHEN: Kök endpoint'e GET isteği atılır
        response = await async_client.get("/")

        # THEN: Cevap beklendiği gibi olmalı
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to the LLM API!"}