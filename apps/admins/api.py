from fastapi import APIRouter
from fastapi.responses import JSONResponse

from apps.admins.repositories import AdminRepository
from apps.admins.schemas import AdminSchema


admin_router = APIRouter()


@admin_router.post("/admin/add")
async def add_admin(req: AdminSchema):
    admin_dict = req.dict(exclude_unset=True)
    repo = AdminRepository()
    result = await repo.insert_admin(admin_dict)
    if result == True:
        return req
    else:
        return JSONResponse(content={'message' : 'update trainer profile problem encountered'}, status_code=500)


@admin_router.post("/admin/login/list")
async def list_admin_login():
    repo = AdminRepository()
    result = await repo.get_all_admin()
    return result
