from pydantic import BaseModel
from datetime import datetime


class LoginSchema(BaseModel):
    id: int
    title: str
    image: str
    price: float
    categories_id: int
    owner_id: int
    messengers_id: int
    created_at: datetime
    updated_at: datetime
