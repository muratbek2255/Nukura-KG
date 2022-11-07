from fastapi import APIRouter
from apps.admins.api import admin_router
from apps.companies.api import company_router
from apps.customers.api import customer_router
from apps.billings.api import billing_router

api_router = APIRouter()

api_router.include_router(billing_router, prefix='/billing', tags=["billing"])
api_router.include_router(admin_router, prefix='/admin', tags=["admin"])
api_router.include_router(company_router, prefix='/company', tags=["company"])
api_router.include_router(customer_router, prefix='/customer', tags=["customer"])
