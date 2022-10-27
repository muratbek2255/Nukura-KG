import ormar

from apps.base.base_model import Login
from db.session import MainMata


class Admin(Login):
    class Meta(MainMata):
        tablename = 'admins'
    is_staff: bool = ormar.Boolean(default=False)
    is_superuser: bool = ormar.Boolean(default=False)
