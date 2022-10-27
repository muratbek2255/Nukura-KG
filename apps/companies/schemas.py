from apps.login.base_schemas import LoginSchema


class CompanySchema(LoginSchema):
    name: str
    full_name: str
    address: str
    email: str
    phone_number: str

    class Config:
        orm_mode = True
