import ormar
from datetime import datetime

from apps.base.base_model import BaseModel
from apps.categories.models import Category
from db.session import MainMata


class Sales(BaseModel):
    class Meta(MainMata):
        tablename = "sales"
    products_id: int = ormar.ForeignKey(to=Category, unique=False, index=False, nullable=False)
    copies_issued: int = ormar.Integer(unique=False, index=False, nullable=False)
    copies_sold: int = ormar.Integer(unique=False, index=False, nullable=False)
    date_issued: datetime = ormar.DateTime(unique=False, index=False, nullable=False)
    revenue: float = ormar.Float(unique=False, index=False, nullable=False)
    profit: float = ormar.Float(unique=False, index=False, nullable=False)
