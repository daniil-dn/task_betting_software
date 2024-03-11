## Setup & Run 🏃‍

```bash
docker-compose up --build

```

After first run:

1) Run migrations
   alembic revision --autogenerate -m "Migration"
   alembic upgrade head
2) Run python pre_start_fill_db.py to fill db with statuses

Test:
Для тестирования можно зайти в любой контейнер и запустить pytest


1. Выбрал связь между микросервисами по http. Все-таки rabbit в данном случае избыточен, но с другой стороны идеально
   подошел бы
2. В качестве воркера для line_provider выбрал APSheduler. Для воркера на arq надо поднимать соседний контейнер.
   Можно сделать, но сейчас для одного воркера будет избыточно хранить таску в редисе

   Visit  (http://localhost:9090/docs, http://localhost:9091/docs) for the interactive FastAPI docs!
