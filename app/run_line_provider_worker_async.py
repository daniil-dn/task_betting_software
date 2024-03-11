import asyncio

from app.arq_redis.worker import create_worker
from app.line_provider.rq.workers import WorkerProcessEventsSettings
from app.logs import server_log

server_log.info('Sentry is ON')


async def main():
    worker_process_events = create_worker(WorkerProcessEventsSettings)
    tasks = [
        worker_process_events.async_run(),
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
