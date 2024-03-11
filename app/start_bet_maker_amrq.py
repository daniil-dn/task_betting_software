import asyncio

from app.bet_maker.armq_service import Consumer

if __name__ == '__main__':
    asyncio.run(Consumer().run())
