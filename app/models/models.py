#  ________________________
#  Import LIBRARIES
from enum import Enum

from pydantic import BaseModel

#  Import FILES
#  ________________________


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# # Define a Pydantic model for request body validation
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool | None = None
