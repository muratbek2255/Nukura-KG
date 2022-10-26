from apps.base.base_schemas import LoginSchema


class AdminReq(LoginSchema):
    is_staff: bool
    is_superuser: bool
