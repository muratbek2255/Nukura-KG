import ormar
from db.session import MainMata


class BaseModel(ormar.Model):
    """
    Base model
    """
    class Meta(MainMata):
        pass

    id: int = ormar.Integer(primary_key=True)


class Login(BaseModel):
    """
    Login model
    """
    class Meta(MainMata):
        tablename = "login"
    username: str = ormar.String(max_length=100, unique=True)
    password: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
    is_active: bool = ormar.Boolean(default=False)
    created_at = ormar.DateTime()
    updated_at = ormar.DateTime()

    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)
