import ormar

from apps.base.base_model import BaseModel
from db.session import MainMata


class Category(BaseModel):

    class Meta(MainMata):
        tablename = "categories"

    title: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
