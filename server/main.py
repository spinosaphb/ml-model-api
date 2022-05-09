"""
Main file
"""
from os.path import join, dirname
import logging
import uvicorn

from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
from dotenv import load_dotenv

DOTENV_PATH = join(dirname(__file__), '.env')
load_dotenv(DOTENV_PATH)

from db.mongodb_utils import close_mongo_connection, connect_to_mongo
from core.config import API_PREFIX, OPENAPI_URL, DOCS_URL, REDOC_URL
from routers import router as api_router

gunicorn_logger = logging.getLogger("gunicorn")

app = FastAPI()

app = FastAPI(
    title="Dell Lead Test API",
    description="API with services for Machine Learning Models",
    version="0.0.1",
    openapi_url=OPENAPI_URL,
    docs_url=DOCS_URL,
    redoc_url=REDOC_URL,
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(api_router, prefix=API_PREFIX)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
else:
    logging.info("------------------ Application Started -------------------")
    fastapi_logger.setLevel(gunicorn_logger.level)
