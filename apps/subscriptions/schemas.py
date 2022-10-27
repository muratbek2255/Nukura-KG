from pydantic import BaseModel
from datetime import datetime


class SubscriptionReq(BaseModel):
    id: int
    customer_id: int
    branch: str
    price: float
    qty: int
    date_purchased: datetime
