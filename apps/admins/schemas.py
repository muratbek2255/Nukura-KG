from datetime import datetime

from pydantic import BaseModel


class AdminSchema(BaseModel):
    """Pydantic model for Admin"""
    id: int
    username: str
    password: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    is_staff: bool
    is_superuser: bool
    role: str

    class Config:
        orm_mode = True
