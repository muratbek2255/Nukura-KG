from apps.base.base_schemas import LoginSchema


class AdminSchema(LoginSchema):
    is_staff: bool
    is_superuser: bool
