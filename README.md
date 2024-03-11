## Setup & Run 🏃‍

```bash
docker-compose up --build

```

After first run:

1) docker exec -ti task_betting_software-app_line_provider-1 bash
2) Run migrations
   alembic revision --autogenerate -m "Migration"
   alembic upgrade head
3) Run script to fill db with statuses 
   python app/pre_start_fill_db.py
4) Run pytest - for testing

Test:
Для тестирования можно зайти в любой контейнер и запустить pytest

1. Выбрал связь между микросервисами по http. Все-таки rabbit в данном случае избыточен, но с другой стороны идеально
   подошел бы
2. В качестве воркера для line_provider выбрал APSheduler. Для воркера на arq надо поднимать соседний контейнер.
   Можно сделать, но сейчас для одного воркера будет избыточно хранить таску в редисе

   Visit  (http://localhost:9090/docs, http://localhost:9091/docs) for the interactive FastAPI docs!
