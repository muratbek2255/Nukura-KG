import ormar
from datetime import datetime

from apps.base.base_model import BaseModel
from apps.categories.models import Category
from apps.companies.models import Company
from apps.messengers.models import Messenger
from db.session import MainMata


class Product(BaseModel):
    class Meta(MainMata):
        tablename = "products"
    title: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
    image: str = ormar.String(max_length=500, unique=False, index=False, nullable=False)
    price: float = ormar.Decimal(maximum=7, decimal_places=2, unique=False, index=False, nullable=False)
    categories_id: int = ormar.ForeignKey(to=Category, unique=False, index=False, nullable=False)
    owner_id: int = ormar.ForeignKey(to=Company, unique=False, index=False, nullable=False)
    messengers_id: int = ormar.ForeignKey(to=Messenger, unique=False, index=False, nullable=False)
    created_at = ormar.DateTime()
    updated_at = ormar.DateTime()
