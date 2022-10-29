from typing import Dict, Any

from apps.customers.models import Customer


class CustomerRepository:
    """CRUD by pattern REPOSITORY"""
    async def insert_customer(self, details: Dict[str, Any]):
        customer = await Customer.objects.create(**details)
        return customer

    async def update_customer(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            customer = await Customer.objects.get(pk=id)
            await customer.update(**details)
        except Exception as e:
            return False
        return True

    async def delete_customer(self, id: int) -> bool:
        try:
            customer = await Customer.objects.get(pk=id)
            await customer.delete()
        except Exception as e:
            return False
        return True

    async def get_all_customer(self):
        return await Customer.objects.all()

    async def get_customer(self, id: int):
        return await Customer.objects.get(pk=id)
