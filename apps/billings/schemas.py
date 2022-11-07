from pydantic import BaseModel
from datetime import datetime


class BillingSchema(BaseModel):
    id: int
    payable: float
    approved_by: str
    date_approved: datetime
    date_billed: datetime
    received_by: str
    date_received: datetime
    total_issues: int
    companies_id: int
    admins_id: int

    class Config:
        orm_mode = True
