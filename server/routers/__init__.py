from fastapi import APIRouter

from routers import mlmodel

router = APIRouter()
router.include_router(mlmodel.router)
