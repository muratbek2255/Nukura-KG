from datetime import date, time
from typing import List, Dict, Any

from apps.admins.models import Admin
from apps.billings.models import Billing
from apps.companies.models import Company


class BillingRepository:

    async def insert_billing(self, details: Dict[str, Any]):
        billing = await Billing.objects.create(**details)
        return billing


    async def update_billing(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            billing = await Billing.objects.get(pk=id)
            await billing.update(**details)
        except:
            return False
        return True

    async def delete_billing(self, id: int) -> bool:
        try:
            billing = await Billing.get(pk=id)
            await billing.delete()
        except Exception as e:
            return False
        return True

    async def get_all_billing(self):
        return await Billing.objects.all()

    async def get_billing(self, id: int):
        return await Billing.objects.get(pk=id)


class BillingAdminRepository:
    # isn't working
    async def join_billing_admin(self, id: int):
        query = Admin.objects.filter(pk=id).prefetch_related('billings')
        result = await query.load()
        return result


class BillingVendorRepository:
    # isn't working
    async def join_billing_vendor(self):
        query = Company.objects.filter(pk=id).prefetch_related('billings')
        result = await query.load(Billing).all()
        return result
