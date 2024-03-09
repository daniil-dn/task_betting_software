## Setup & Run 🏃‍

```bash
docker-compose up --build

```

After first run:

1) Run migrations
   alembic upgrade head
   alembic revision --autogenerate -m "Migration"

Visit  (http://localhost:9090/docs, http://localhost:9091/docs) for the interactive FastAPI docs!