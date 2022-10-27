import ormar
from datetime import datetime

from apps.base.base_model import BaseModel
from apps.customers.models import Customer
from db.session import MainMata


class Subscription(BaseModel):
    class Meta(MainMata):
        tablename = "subscriptions"
    customer_id: int = ormar.ForeignKey(to=Customer, unique=False, index=False, nullable=False)
    branch: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
    price: str = ormar.Float(unique=False, index=False, nullable=False)
    qty: str = ormar.Integer(unique=False, index=False, nullable=False)
    date_purchased: datetime = ormar.DateTime(unique=False, index=False, nullable=False)
