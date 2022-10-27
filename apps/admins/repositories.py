from typing import Dict, Any

from apps.admins.models import Admin


class AdminRepository:
    """CRUD by pattern REPOSITORY"""
    async def insert_admin(self, details: Dict[str, Any]):
        admin = await Admin.objects.create(**details)
        return admin

    async def update_admin(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            admin = await Admin.objects.get(pk=id)
            await admin.update(**details)
        except Exception as e:
            return False
        return True

    async def delete_admin(self, id: int) -> bool:
        try:
            admin = await Admin.objects.get(pk=id)
            await admin.delete()
        except Exception as e:
            return False
        return True

    async def get_all_admin(self):
        return await Admin.objects.all()

    async def get_admin(self, id: int):
        return await Admin.objects.get(pk=id)
