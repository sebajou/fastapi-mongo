from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from config.settings import Settings
import models as models

settings = Settings()


async def initiate_database():
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    await init_beanie(
        database=client.get_default_database("student_db"),
        document_models=models.__all__
    )
