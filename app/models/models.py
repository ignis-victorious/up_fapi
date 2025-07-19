#  ________________________
#  Import LIBRARIES
from pydantic import BaseModel

#  Import FILES
#  ________________________


# Define a Pydantic model for request body validation
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None
