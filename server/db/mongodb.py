from motor.motor_asyncio import AsyncIOMotorClient

class DataBase:
    """
    Mongo Data Base
    """
    client: AsyncIOMotorClient = None

db = DataBase()

async def get_database() -> AsyncIOMotorClient:
    """
    Return client database
    """
    return db.client