import ormar

from apps.base.base_model import Login
from db.session import metadata, database


class Customer(Login):

    class Meta(ormar.ModelMeta):
        tablename = 'customers'
        metadata = metadata
        database = database

    firstname: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
    lastname: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
    address: str = ormar.String(max_length=100, unique=False, index=False, nullable=False)
    email: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
    phone_number: str = ormar.String(max_length=127, unique=False)
