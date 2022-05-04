from pymongo import MongoClient

class DataBase:
    """
    Mongo Data Base
    """
    client: MongoClient = None

db = DataBase()

async def get_database() -> MongoClient:
    """
    Return client database
    """
    return db.client