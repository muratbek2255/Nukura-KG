from typing import Dict, Any

from apps.companies.models import Company


class CompanyRepository:
    """CRUD by pattern REPOSITORY"""
    async def insert_company(self, details: Dict[str, Any]):
        admin = await Company.objects.create(**details)
        return admin

    async def update_company(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            admin = await Company.objects.get(pk=id)
            await admin.update(**details)
        except Exception as e:
            return False
        return True

    async def delete_company(self, id: int) -> bool:
        try:
            admin = await Company.objects.get(pk=id)
            await admin.delete()
        except Exception as e:
            return False
        return True

    async def get_all_company(self):
        return await Company.objects.all()

    async def get_company(self, id: int):
        return await Company.objects.get(pk=id)
