from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasic

from apps.admins.repositories import AdminRepository
from apps.admins.schemas import AdminSchema
from apps.admins.services import process_billing
from apps.base import base_service
from apps.billings.repositories import BillingAdminRepository

http_basic = HTTPBasic()

admin_router = APIRouter()


@admin_router.post("/admin/add", dependencies=[Depends(base_service.check_admin)])
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


@admin_router.put("/admin/login/list", dependencies=[Depends(base_service.check_admin)])
async def update_admin_login(id: int, req: AdminSchema):
    """For update admins"""
    admin_req = req.dict(exclude_unset=True)
    repo = AdminRepository()
    result = await repo.update_admin(id, admin_req)
    return result


@admin_router.delete("/admin/login/list", dependencies=[Depends(base_service.check_admin)])
async def delete_admin_login(id: int):
    """For update admins"""
    repo = AdminRepository()
    result = await repo.delete_admin(id)
    return result


@admin_router.get("/admin/billing/all")
async def list_admin_with_billing(id: int):
    repo = BillingAdminRepository()
    result = await repo.join_billing_admin(id)
    data = await process_billing(result)
    return jsonable_encoder(data)
