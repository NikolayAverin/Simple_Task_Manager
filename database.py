from typing import Optional

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine("sqlite+aiosqlite:///tasks.db")

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class TaskOrm(Model):
    """Модель таблицы"""

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


async def create_tables():
    """Функция создания таблицы."""
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    """Функция удаления таблицы."""
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
