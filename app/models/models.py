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


# Define a Pydantic model for request body validation
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None
