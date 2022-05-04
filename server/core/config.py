"""
Environment variables module
"""
from os import getenv

API_PREFIX = "/api/lead"

MONGODB_URL = getenv('MONGODB_URL', "")
MAX_CONNECTIONS_COUNT = int(getenv("MAX_CONNECTIONS_COUNT", None) or 10)
MIN_CONNECTIONS_COUNT = int(getenv("MIN_CONNECTIONS_COUNT", None) or 10)

OPENAPI_URL = API_PREFIX + "/openapi.json" 
DOCS_URL = API_PREFIX + "/doc" 
REDOC_URL = API_PREFIX + "/docs" 
