from apps.base.base_schemas import LoginSchema


class CustomerSchema(LoginSchema):
    firstname: str
    lastname: str
    address: str
    email: str
    phone_number: str
