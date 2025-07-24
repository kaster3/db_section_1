import asyncio
import logging

from app.db.db_helper import db_helper
from app.db.models.base import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def init_models() -> None:
    logger.info("Таблицы для создания:")
    for table in Base.metadata.tables.values():
        logger.info("%s", table.name)

    logger.info("Попытка подключения к базе данных...")
    try:
        async with db_helper.engine.begin() as connection:
            logger.info("Подключение успешно установлено")
            await connection.run_sync(Base.metadata.create_all)
            logger.info("Таблицы созданы!!!")
    except Exception as e:
        logger.error(f"Ошибка при создании таблиц: {e}")


async def main() -> None:
    await init_models()


if __name__ == "__main__":
    asyncio.run(main())

