import pytest_asyncio
from httpx import ASGITransport, AsyncClient

import main
from main import app, tasks

@pytest_asyncio.fixture
async def client():
    main.tasks.clear()
    main.nex_id = 1
    async with AsyncClient(transport = ASGITransport(app=app), base_url= "htpp://test",) as c:
        yield c
