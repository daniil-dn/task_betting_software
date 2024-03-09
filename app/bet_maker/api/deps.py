import aio_pika

from app.core.config import settings


async def get_armq(timeout=None):
    connection = await aio_pika.connect_robust(settings.ARMQ_URL, timeout=timeout)
    channel = await connection.channel()
    return connection, channel
