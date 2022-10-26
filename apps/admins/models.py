import ormar

from apps.base.base_model import Login
from db.session import MainMata


class Admin(Login):
    class Meta(MainMata):
        tablename = "admins"
    is_staff: bool = ormar.Boolean(default=False)
    is_superuser: bool = ormar.Boolean(default=False)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)
