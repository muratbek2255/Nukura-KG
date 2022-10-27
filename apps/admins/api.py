from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic

from apps.admins.repositories import AdminRepository
from apps.admins.schemas import AdminSchema
from apps.base import base_service

http_basic = HTTPBasic()

admin_router = APIRouter()


@admin_router.post("/admin/add")
async def add_admin(req: AdminSchema):
    """For add admin"""
    admin_req = req.dict(exclude_unset=True)
    repo = AdminRepository()
    result = await repo.insert_admin(details=admin_req)
    return result


@admin_router.post("/admin/login/list", dependencies=[Depends(base_service.check_admin)])
async def list_admin_login():
    """For list admins"""
    repo = AdminRepository()
    result = await repo.get_all_admin()
    return result
