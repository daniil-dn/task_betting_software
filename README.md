## Setup & Run 🏃‍

```bash
docker-compose up --build

```

After first run:

1) Run migrations
   alembic upgrade head
   alembic revision --autogenerate -m "Migration"
2) Run python pre_start_fill_db.py to fill db with statuses

Visit  (http://localhost:9090/docs, http://localhost:9091/docs) for the interactive FastAPI docs!

1. выбрал связь между микросервисами по http. Все-таки rabbit в данном случае изыточен
2. вопрос по архитектуре задавал через Дарью.
3. В качестве воркера для line_provider выбрал APSheduler. Для воркера на arq надо было бы поднимать соседний контейнер.
   я такое делал, но сейчас для одного воркера будет избыточно хранить таску в редисе 
