import os

from celery import Celery
from celery.utils.log import get_task_logger
from local_settings import SECRET_KEY

PROJECT_NAME = "App"
SERVER_HOST = 'http://127.0.0.1:8080'

# Secret key
SECRET_KEY = SECRET_KEY

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_V1_STR = "/api/v1"

# Token 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

# CORS
BACKEND_CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:8080",
]
