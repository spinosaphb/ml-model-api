"""
CRUD Machine Learning Models
"""
from bson import ObjectId
from pymongo.collection import Collection
from db.mongodb import AsyncIOMotorClient
from core.config import DATABASE_NAME, MODEL_COLLECTION_NAME
from core.utils import handle_create_result

async def get_all_models(
    conn: AsyncIOMotorClient, page: int,
    page_size: int, query: dict = None, projection: dict = None):
    """Get all models"""

    collection = conn[DATABASE_NAME][MODEL_COLLECTION_NAME]
    result = collection.find(query, projection)\
        .skip((page - 1) * page_size).limit(page_size)

    return await result.to_list(length = None)


async def get_model(
    conn: AsyncIOMotorClient, query: dict = None,
    projection: dict = None) -> dict:
    """Get model"""

    result = conn[DATABASE_NAME][MODEL_COLLECTION_NAME].\
        find_one(query, projection)

    return await result


async def create_model(conn: AsyncIOMotorClient, mlmodel: dict):
    """Create model"""
    print('mlmodel:')
    print(mlmodel)
    result = await conn[DATABASE_NAME][MODEL_COLLECTION_NAME].\
        insert_one(mlmodel)

    return handle_create_result(result)


async def update_model(conn: AsyncIOMotorClient, mlmodel: dict, model_id: str):
    """Update Model"""
    collection: Collection = conn[DATABASE_NAME][MODEL_COLLECTION_NAME]
    result = await collection.update_one({'_id': ObjectId(model_id)}, {'$set': mlmodel})
    return result


async def delete_model_by_id(conn: AsyncIOMotorClient, model_id: str):
    """Delete Model"""
    collection: Collection = conn[DATABASE_NAME][MODEL_COLLECTION_NAME]
    result = await collection.delete_one({'_id': ObjectId(model_id)})
    return result
