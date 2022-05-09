"""
Mongo DB utils module
"""

from core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from db.mongodb import db, AsyncIOMotorClient

def connect_to_mongo():
    """Make connection"""

    print(MONGODB_URL)
    try:
        print(f'mongo url: {MONGODB_URL}\n')
        db.client = AsyncIOMotorClient(
            str(MONGODB_URL),
            maxPoolSize=MAX_CONNECTIONS_COUNT,
            minPoolSize=MIN_CONNECTIONS_COUNT
        )
    except Exception as ex:
        raise Exception(ex, "Erro ao conectar o banco") from ex

def close_mongo_connection():
    """Close conection"""
    db.client.close() 