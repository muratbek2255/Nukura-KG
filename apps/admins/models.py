import ormar

from apps.base.base_model import Login
from db.session import metadata, database


class Admin(Login):

    class Meta(ormar.ModelMeta):
        tablename = 'admins'
        metadata = metadata
        database = database

    is_staff: bool = ormar.Boolean(default=False)
    is_superuser: bool = ormar.Boolean(default=False)
