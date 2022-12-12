"""
Machine Learning Model route
"""
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services import mlmodel as mlmodel_service
from db.mongodb import get_database
from models.mlmodel import MLModel, MLModelResponse
from typing import Optional, List
from pymongo.results import DeleteResult

router = APIRouter()

@router.post("/modelo/", tags=['Model'], response_model=MLModelResponse, responses={201: {"model": MLModelResponse}})
async def create_model(model: MLModel, database = Depends(get_database)):
    """
    Create model
    """
    result = await mlmodel_service.create_model(database, model)
    model_response = MLModelResponse(**model.dict()) 
    model_response.id = result['id']
    content = jsonable_encoder(model_response)

    return JSONResponse(content=content, status_code=status.HTTP_201_CREATED)


@router.get("/modelo/", tags=['Model'], response_model=List[MLModelResponse])
async def get_models(
    page: Optional[int] = 1,
    page_size: Optional[int] = 0,
    database = Depends(get_database)):
    """Return all models.

    Keyword arguments:
        name -- name of models to be returned
        page -- specify page
        page_size -- specify page size
    """
    response = mlmodel_service.get_models(database, page, page_size)
    return [MLModelResponse(**item) async for item in response]



@router.get("/modelo/{name}", tags=['Model'])
async def get_model_by_name(name: str = None, database = Depends(get_database)):
    """
    Return model by name
    """
    response = await mlmodel_service.get_model(database, projection={
        'name': 1,
        'description':1,
        '_id':0
    }, name=name)

    return response


@router.put("/modelo/{model_id}", tags=['Model'])
async def update_model(model_id, mlmodel: MLModel, database = Depends(get_database)):
    """
    Update Model
    """
    response = await mlmodel_service.update_model(database, mlmodel, model_id)
    return response


@router.delete("/modelo/{model_id}", tags=['Model'])
async def delete_model(model_id, database = Depends(get_database)):
    """
    Delete Model
    """
    response: DeleteResult = await mlmodel_service.delete_model(database, model_id)
    return {'deleted_count': response.deleted_count}
