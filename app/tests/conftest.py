from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.db.session import SessionLocal
from app.logs import tests_log
from app.start_bet_maker import app


@pytest.fixture(scope="session")
def db() -> Generator:
    tests_log.info("CREATE DB")
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    tests_log.info("CREATE client")
    with TestClient(app) as c:
        yield c
