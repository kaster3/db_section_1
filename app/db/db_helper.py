import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


class DataBaseHelper:
    def __init__(self, url: str) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
        )


env_path = Path(__file__).parent.parent.parent / ".template.env"
load_dotenv(env_path)

DB_URL = os.getenv("DB_URL")
if not DB_URL:
    raise ValueError("DB_URL не найден в .env файле!")

db_helper = DataBaseHelper(url=DB_URL)
