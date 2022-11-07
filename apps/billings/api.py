from datetime import date

from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi.responses import JSONResponse

from apps.billings.repositories import BillingRepository, BillingVendorRepository
from apps.billings.schemas import BillingSchema
from apps.billings.services import generate_billing_sheet, create_total_payables_year, create_total_payables_year_celery

billing_router = APIRouter()


@billing_router.post("/billing/add")
async def add_billing(req: BillingSchema):
    billing_dict = req.dict(exclude_unset=True)
    repo = BillingRepository()
    result = await repo.insert_billing(billing_dict)
    return result


@billing_router.post("/billing/save/csv")
async def save_vendor_billing(billing_date: date, tasks: BackgroundTasks):
    repo = BillingVendorRepository()
    result = await repo.join_billing_vendor()
    tasks.add_task(generate_billing_sheet, billing_date, result)
    tasks.add_task(create_total_payables_year, billing_date, result)
    return {"message": "done"}


@billing_router.post("/billing/total/payable")
async def compute_payable_yearly(billing_date: date):
    repo = BillingVendorRepository()
    result = await repo.join_billing_vendor()
    total_result = create_total_payables_year_celery.apply_async(queue='default', args=(billing_date, result))
    total_payable = total_result.get()

    return {"total_payable": total_payable}
