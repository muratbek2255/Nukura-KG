import ormar
from datetime import datetime

from apps.admins.models import Admin
from apps.base.base_model import BaseModel
from apps.companies.models import Company
from db.session import MainMata


class Billing(BaseModel):
    class Meta(MainMata):
        tablename = "billings"
    payable: float = ormar.Float(unique=False, index=False, nullable=False)
    approved_by: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
    date_approved: datetime = ormar.DateTime(unique=False, index=False, nullable=False)
    date_billed: datetime = ormar.DateTime(unique=False, index=False, nullable=False)
    received_by: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
    date_received: datetime = ormar.DateTime(unique=False, index=False, nullable=False)
    total_issues: int = ormar.Integer(unique=False, index=False, nullable=False)
    companies_id: int = ormar.ForeignKey(to=Company, unique=False, index=False, nullable=False)
    admins_id: int = ormar.ForeignKey(to=Admin, unique=False, index=False, nullable=False)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)
