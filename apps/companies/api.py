from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic

from apps.companies.repositories import CompanyRepository
from apps.companies.schemas import CompanySchema
from apps.base import base_service

http_basic = HTTPBasic()

admin_router = APIRouter()


@admin_router.post("/admin/add", dependencies=[Depends(base_service.check_admin)])
async def add_company(req: CompanySchema):
    """For add admin"""
    admin_req = req.dict(exclude_unset=True)
    repo = CompanyRepository()
    result = await repo.insert_company(details=admin_req)
    return result


@admin_router.post("/admin/login/list", dependencies=[Depends(base_service.check_admin)])
async def list_company_login():
    """For list admins"""
    repo = CompanyRepository()
    result = await repo.get_all_company()
    return result


@admin_router.put("/admin/login/list", dependencies=[Depends(base_service.check_admin)])
async def update_admin_login(id: int, req: CompanySchema):
    """For update admins"""
    admin_req = req.dict(exclude_unset=True)
    repo = CompanyRepository()
    result = await repo.update_company(id, admin_req)
    return result


@admin_router.delete("/admin/login/list", dependencies=[Depends(base_service.check_admin)])
async def delete_admin_login(id: int):
    """For update admins"""
    repo = CompanyRepository()
    result = await repo.delete_company(id)
    return result
