import asyncio

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasic

from apps.customers.repositories import CustomerRepository
from apps.customers.schemas import CustomerSchema
from apps.base import base_service
from apps.customers.services import count_login, build_user_list

http_basic = HTTPBasic()

customer_router = APIRouter()


@customer_router.post("/customer/add", dependencies=[Depends(base_service.check_admin)])
async def add_customer(req: CustomerSchema):
    """For add customer"""
    admin_req = req.dict(exclude_unset=True)
    repo = CustomerRepository()
    result = await repo.insert_customer(details=admin_req)
    return result


@customer_router.post("/customer/login/list", dependencies=[Depends(base_service.check_admin)])
async def list_customer_login():
    """For list customers"""
    repo = CustomerRepository()
    result = await repo.get_all_customer()
    return result


@customer_router.put("/customer/login/list", dependencies=[Depends(base_service.check_admin)])
async def update_customer_login(id: int, req: CustomerSchema):
    """For update customers"""
    admin_req = req.dict(exclude_unset=True)
    repo = CustomerRepository()
    result = await repo.update_customer(id, admin_req)
    return result


@customer_router.delete("/customer/login/list", dependencies=[Depends(base_service.check_admin)])
async def delete_customer_login(id: int):
    """For update customers"""
    repo = CustomerRepository()
    result = await repo.delete_customer(id)
    return result


@customer_router.get("/login/list/records")
async def list_login_records():
    repo = CustomerRepository()
    login_data = await repo.get_all_customer()
    result = await asyncio.gather(count_login(login_data), build_user_list(login_data))
    data = jsonable_encoder(result[1])
    return {'num_rec': result[0], 'user_list': data}
