import ormar

from apps.base.base_model import Login
from db.session import MainMata


class Company(Login):
    class Meta(MainMata):
        tablename = "companies"
    name: str = ormar.String(max_length=56, unique=False, index=False, nullable=False)
    full_name: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
    address: str = ormar.String(max_length=100, unique=False, index=False, nullable=False)
    email: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
    phone_number: str = ormar.String(max_length=127, unique=False)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)