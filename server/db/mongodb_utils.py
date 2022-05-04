"""
Mongo DB utils module
"""

from pymongo import MongoClient
from core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from db.mongodb import db


def connect_to_mongo():
    try:
        db.client = MongoClient(
            str(MONGODB_URL),
            maxPoolSize=MAX_CONNECTIONS_COUNT,
            minPoolSize=MIN_CONNECTIONS_COUNT
        )
    except Exception as ex:
        BotMessage().send_message(
            "Hnerd em " + MODE + ", não está conseguindo se conectar ao Mongo!!! " + str(ex)
        )

def close_mongo_connection():
    db.client.close() 