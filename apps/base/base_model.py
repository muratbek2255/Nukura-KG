import ormar
from db.session import MainMata


class BaseModel(ormar.Model):
    """
    Base model
    """
    class Meta(MainMata):
        abstract = True

    id: int = ormar.Integer(primary_key=True)


class Login(ormar.Model):
    """
    Login model
    """

    class Meta(MainMata):
        abstract = True

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=100, unique=True)
    password: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
    is_active: bool = ormar.Boolean(default=False)
    created_at = ormar.DateTime()
    updated_at = ormar.DateTime()
