from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import delete_tables, create_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Функция, которая удаляет старую таблицу и создаёт новую при вызове."""
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
