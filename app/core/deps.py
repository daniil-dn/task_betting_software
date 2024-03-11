from typing import Generator

import aio_pika

from app.core.config import settings
from app.db import SessionLocal


async def get_armq(timeout=None):
    connection = await aio_pika.connect_robust(settings.ARMQ_URL, timeout=timeout)
    return connection


async def get_db() -> Generator:
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
