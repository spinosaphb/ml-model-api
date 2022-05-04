"""
Machine Learning Model route
"""
from fastapi import APIRouter
from services import mlmodel
from db.mongodb import get_database


router = APIRouter(dependencies=get_database)

@router.get("modelo/", tags=['Model'])
def get_models(name: str = None, page: int = None, page_size: int = None):
    """Return all models.

    Keyword arguments:
    name -- name of models to be returned
    page -- specify page
    page_size -- specify page size
    """
    return mlmodel.get_models(*(router.dependencies), name, page, page_size)
