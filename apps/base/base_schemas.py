from pydantic import BaseModel
from datetime import datetime


class LoginSchema(BaseModel):
    id: int
    username: str
    password: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
