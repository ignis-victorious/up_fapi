#  ________________________
#  Import LIBRARIES
import re
from datetime import date, datetime
from typing import Annotated, NewType

from pydantic import BaseModel, EmailStr, Field, field_validator

#  Import FILES
#  ________________________


# class User(BaseModel):
#     id: int
#     name: str
#     email: str
#     is_active: bool = True
#     created_at: datetime = datetime.now()
#     tags: list[str] = []
#     profile_picture: str | None = None


class Product(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)  # Must be greater than 0
    in_stock: bool = True
    tags: list[str] = []
    description: str = Field(min_length=10, max_length=1000)
    contact_email: EmailStr  # Specialized email validation part of Pydantic
    quantity: Annotated[int, Field(ge=0)]  # Must be greater than or equal to 0


class SignupForm(BaseModel):
    username: str
    password1: str
    password2: str

    @field_validator("username")
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        if not v.isalnum():
            raise ValueError("Username must be alphanumeric")
        return v


#     @field_validator("password2")
#     @classmethod
#     def passwords_match(cls, v: str, info) -> str:
#         if "password1" in info.data and v != info.data["password1"]:
#             raise ValueError("Passwords do not match")
#         return v


# class Order(BaseModel):
#     items: list[str]
#     item_count: int

#     @model_validator(mode="after")
#     def check_item_count(self) -> Order:
#         if len(self.items) != self.item_count:
#             raise ValueError("Item count does not match number of items")
#         return self


class Article(BaseModel):
    id: int
    title: str
    content: str
    published: datetime
    tags: list[str] = []


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)


class UserResponse(BaseModel):
    id: int
    username: str
    email: str


# Option 1: Using NewType with Pydantic validators
UserId = NewType("UserId", str)


class User(BaseModel):
    id: UserId
    name: str

    @field_validator("id")
    @classmethod
    def validate_user_id(cls, v: str) -> str:
        if not re.match(pattern=r"^USER_\d[6]$", string=v):
            raise ValueError("User ID must be in format USER_XXXXXX")
        return v


# Option 2: Using Annotated with Field constraints
ISBN = Annotated[
    str, Field(pattern=r"^(?=(?:\D*\d) {10} {?:(?:\D*\d} {3})?$) [\d-] +$")
]


class Book(BaseModel):
    title: str
    isbn: ISBN


def validate_future_date(value: date) -> date:
    if value <= date.today():
        raise ValueError("Date must be in the future")
    return value


class Event(BaseModel):
    name: str
    event_date: date

    @field_validator("event _date")
    @classmethod
    def check_future_date(cls, v: date) -> date:
        return validate_future_date(value=v)
