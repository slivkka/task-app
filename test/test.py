import pytest
import pytest_asyncio

from httpx import AsyncClient, ASGITransport
from tortoise import Tortoise


from main import app
from src.app.db.models.users import User
from src.app.repositories.users import ph
from src.core.config import settings


@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport,
                           base_url="http://test") as client:
        await Tortoise.init(config=settings.TORTOISE_ORM_TEST)
        await Tortoise.generate_schemas()

        yield client

        await Tortoise._drop_databases()


@pytest.mark.asyncio
async def test_register_user_success(client):
    payload = {
        "username": "chucha111111",
        "email": "cedar@gmail.com",
        "hashed_password": "cedar"
    }
    response = await client.post("/auth/register", json=payload)
    assert response.status_code == 200
    assert response.json()[0]["username"] == "chucha111111"



@pytest.mark.asyncio
async def test_login(client):
    await User.get_or_create(
        username="chucha111111",
        hashed_password=ph.hash("cedar"),
        email="cedar@gmail.com"
    )

    payload = {
        "username": "chucha111111",
        "password": "cedar"
    }
    response = await client.post("/auth/login", data=payload)
    assert response.status_code == 200
    assert response.json()["access_token"]


@pytest.mark.asyncio
async def test_refresh_new_access_token(client):
    await User.get_or_create(
        username="chucha111111",
        hashed_password=ph.hash("cedar"),
        email="cedar@gmail.com"
    )

    payload = {
        "username": "chucha111111",
        "password": "cedar"
    }
    response = await client.post("/auth/login", data=payload)

    new_access = await client.post("/auth/logout", json=response.json())
    assert new_access.status_code == 200

