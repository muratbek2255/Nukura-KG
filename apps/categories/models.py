import ormar

from apps.base.base_model import BaseModel
from db.session import MainMata


class Billing(BaseModel):

    class Meta(MainMata):
        tablename = "billings"

    title: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
