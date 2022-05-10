from bson.errors import InvalidId
from models.mlmodel import MLModel
from crud import mlmodel as crud_model
from fastapi.exceptions import HTTPException
from fastapi import status
from pymongo.results import UpdateResult, DeleteResult

async def get_models(
    conn, page: int = 1, page_size: int = 0,
    query = None, projection = None):
    """
    Return all models
    """
    result = await crud_model.get_all_models(conn, page, page_size, query, projection)  
    for item in result:
        item.update({'_id': str(item['_id'])})
        yield item


async def get_model(conn, projection = None, **query):
    """Return model"""
    return await crud_model.get_model(conn, query, projection)


async def create_model(conn, mlmodel: MLModel):
    """
    Create Model
    """
    return await crud_model.create_model(conn, mlmodel.dict())


async def update_model(conn, mlmodel: MLModel, model_id: str):
    """
    Update Model
    """
    model = mlmodel.dict()

    try:
        result: UpdateResult = await crud_model.update_model(conn, model, model_id)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid Id'
        ) from InvalidId

    return {'modified_count': result.modified_count}


async def delete_model(conn, model_id: str):
    result = await crud_model.delete_model_by_id(conn, model_id)
    return result