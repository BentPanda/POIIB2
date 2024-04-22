from pydantic import BaseModel


class Address(BaseModel):
    street: str


class User(BaseModel):
    first_name: str
    last_name: str
    address: Address


