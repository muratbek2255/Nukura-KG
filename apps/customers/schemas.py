from datetime import datetime

from pydantic import BaseModel


class CustomerSchema(BaseModel):
    id: int
    username: str
    password: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    firstname: str
    lastname: str
    address: str
    email: str
    phone_number: str
    role: str

    class Config:
        orm_mode = True
