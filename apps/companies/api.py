from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic

from apps.companies.repositories import CompanyRepository
from apps.companies.schemas import CompanySchema
from apps.base import base_service

http_basic = HTTPBasic()

company_router = APIRouter()


@company_router.post("/company/add", dependencies=[Depends(base_service.check_admin)])
async def add_company(req: CompanySchema):
    """For add company"""
    admin_req = req.dict(exclude_unset=True)
    repo = CompanyRepository()
    result = await repo.insert_company(details=admin_req)
    return result


@company_router.post("/company/login/list", dependencies=[Depends(base_service.check_admin)])
async def list_company_login():
    """For list company"""
    repo = CompanyRepository()
    result = await repo.get_all_company()
    return result


@company_router.put("/company/login/list", dependencies=[Depends(base_service.check_admin)])
async def update_company_login(id: int, req: CompanySchema):
    """For update company"""
    admin_req = req.dict(exclude_unset=True)
    repo = CompanyRepository()
    result = await repo.update_company(id, admin_req)
    return result


@company_router.delete("/company/login/list", dependencies=[Depends(base_service.check_admin)])
async def delete_company_login(id: int):
    """For update company"""
    repo = CompanyRepository()
    result = await repo.delete_company(id)
    return result
