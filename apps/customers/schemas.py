from apps.login.base_schemas import LoginSchema


class CustomerSchema(LoginSchema):
    firstname: str
    lastname: str
    address: str
    email: str
    phone_number: str
