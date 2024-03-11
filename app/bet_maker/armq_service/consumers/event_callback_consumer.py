import asyncio

import aio_pika

from app.core.config import settings
from app.logs import armq_bet_maker_log


class Consumer:
    __slots__ = (
        'connection', 'channel',
    )

    async def run(self):
        armq_bet_maker_log.info(f'ARMQ_URL: {settings.ARMQ_URL}')
        self.connection = await aio_pika.connect_robust(
            settings.ARMQ_URL, timeout=80
        )
        # Creating channel
        self.channel = await self.connection.channel()

        # Declaring queue
        queue = await self.channel.declare_queue(
            'event_callback', durable=True, auto_delete=False
        )
        await queue.consume(self.event_callback)

        try:
            # Wait until terminate
            await asyncio.Future()
        finally:
            await self.connection.close()

    async def event_callback(
            self,
            message: aio_pika.abc.AbstractIncomingMessage,
    ) -> None:
        async with message.process(ignore_processed=True):
            print(message)
