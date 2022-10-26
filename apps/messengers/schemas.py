from pydantic import BaseModel

from datetime import datetime


class MessengerReq(BaseModel):
    id: int
    firstname: str
    lastname: str
    salary: float
    date_employed: datetime
    status: int
    company_id: int
