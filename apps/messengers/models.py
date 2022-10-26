import ormar
from datetime import datetime

from apps.base.base_model import BaseModel
from apps.companies.models import Company
from db.session import MainMata


class Messenger(BaseModel):
    class Meta(MainMata):
        tablename = "messengers"
    firstname: str = ormar.String(max_length=56, unique=False, index=False, nullable=False)
    lastname: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
    salary: float = ormar.Float(unique=False, index=False, nullable=False)
    date_employed: datetime = ormar.DateTime(unique=False, index=False, nullable=False)
    status: int = ormar.Integer(unique=False, index=False, nullable=False)
    companies_id: int = ormar.ForeignKey(to=Company, unique=False, index=False, nullable=False)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)
