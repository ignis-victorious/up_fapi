#  ________________________
#  Import LIBRARIES
from enum import StrEnum

# from enum import Enum
from pydantic import BaseModel, Field

#  Import FILES
#  ________________________


class Category(StrEnum):
    # class Category(str, Enum):
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    BOOKS = "books"
    FOOD = "food"


class ItemBase(BaseModel):
    name: str = Field(default=..., min_length=1, max_length=50)
    description: str | None = Field(default=None, max_length=300)
    price: float = Field(default=..., gt=0)
    tax: float | None = Field(default=None, ge=0)
    category: Category  # This is the key!


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        json_schema_extra: dict[str, dict[str, int | str | float]] = {
            "example": {
                "id": 1,
                "name": "Smartphone",
                "description": "Latest model with high-end features",
                "price": 799.99,
                "tax": 79.99,
                "category": "food",
            }
        }


# {
#   "name": "mamma",
#   "description": "nonna + mamma",
#   "price": 121,
#   "tax": 90,
#   "category": "food",
#   "id": 1
# }
