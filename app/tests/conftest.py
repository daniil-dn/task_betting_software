import asyncio
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.db.session import SessionLocal
from app.logs import tests_log
from app.start_bet_maker import app


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function", autouse=True)
def session():
    tests_log.info("CREATE DB")
    return SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    tests_log.info("CREATE client")
    with TestClient(app) as c:
        yield c
