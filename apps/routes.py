from fastapi import APIRouter
from apps.admins.api import admin_router

api_router = APIRouter()

api_router.include_router(admin_router, prefix='/admin', tags=["admin"])
