#  ________________________
#  Import LIBRARIES
from enum import Enum

from pydantic import BaseModel, field_validator

#  Import FILES
#  ________________________


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# # Define a Pydantic model for request body validation
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


# class Image(BaseModel):
#     url: str
#     name: str


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []
#     image: Image | None = None

# #  Using Field as validator
# class Item(BaseModel):
#     name: str = Field(default=..., min_length=1, max_length=50)
#     description: str | None = Field(default=None, max_length=300)
#     price: float = Field(default=..., gt=0)
#     tax: float | None = Field(default=None, ge=0)


#  Using field_validator as validator
class Item(BaseModel):
    name: str
    price: float
    quantity: int

    @field_validator("quantity")
    def quantity_must_be_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Quantity must be positive")
        return v

    @field_validator("price")
    def price_must_be_positive(cls, v: float) -> float:
        if v < 0:
            raise ValueError("Price must be positive")
        return v
