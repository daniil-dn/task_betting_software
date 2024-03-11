from arq import cron

from app.arq_redis.connections import RedisSettings
from app.core.config import settings
from app.line_provider.rq.process_events import process_event, process_events


class WorkerProcessEventsSettings:
    functions = [process_event]
    queue_name = "process_events_tasks"
    keep_result = 0
    max_jobs = 200
    max_tries = 3
    poll_delay = 1
    job_timeout = 60 * 2

    redis_settings = RedisSettings(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        conn_retry_delay=5,
        conn_retries=20,
        conn_timeout=30,
    )
    cron_jobs = [
        cron(
            process_events, second=1,
            unique=True,
            job_id="process_events", run_at_startup=True
        )
    ]
