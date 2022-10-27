from typing import Dict, Any

from apps.admins.models import Admin


class AdminRepository:

    async def insert_admin(self, details: Dict[str, Any]) -> bool:
        try:
            admin = await Admin.objects.create(**details)
        except Exception as e:
            print(e)
            return False
        return True

    async def update_admin(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            admin = await Admin.objects.get(pk=id)
            await admin.update(**details).apply()
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
