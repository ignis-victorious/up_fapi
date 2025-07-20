#  ________________________
#  Import LIBRARIES
from fastapi import Body, FastAPI, HTTPException, Path, Query

from .data.fake_database import counter, items_db

#  Import FILES
from .models.models import Category, Item, ItemBase, ItemCreate

#  ________________________


app: FastAPI = FastAPI(title="Item Manager API", version="1.0.0")


# Routes
@app.post(path="/items/", response_model=Item, status_code=201)
def create_item(item: ItemCreate) -> Item:
    global counter
    counter += 1
    # Debugging line:
    print(f"Incoming item data (model_dump): {item.model_dump(mode='json')}")

    item_data = item.model_dump(mode="json")
    # item_data: dict[str, str | int | float | None] = item.model_dump(mode="json")
    if "category" not in item_data or item_data["category"] is None:
        raise HTTPException(status_code=422, detail="Category is required")
    new_item: Item = Item(
        id=counter,
        name=item.name,
        description=item.description,
        price=item.price,
        tax=item.tax,
        category=item.category,  # Pass the actual Enum member, not its string representation from model_dump
    )
    # new_item: Item = Item(id=counter, **item_data)
    items_db[counter] = new_item
    return new_item


@app.get(path="/items/", response_model=list[Item])
def read_items(
    skip: int = Query(default=0, ge=0, description="Number of items to skip"),
    limit: int = Query(
        default=10, ge=1, le=100, description="Max number of items to return"
    ),
    category: Category | None = None,
) -> list[ItemBase]:
    filtered_items: list[ItemBase] = list(items_db.values())

    if category:
        filtered_items = [item for item in filtered_items if item.category == category]

    return filtered_items[skip : skip + limit]


@app.get(path="/items/{item_id}", response_model=Item)
def read_item(
    item_id: int = Path(default=..., gt=0, description="The ID of the item to get"),
) -> ItemBase:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not. found")
    return items_db[item_id]


@app.put(path="/items/(item_id)", response_model=Item)
def update_item(
    item_id: int = Path(default=..., gt=0),
    item: ItemBase = Body(
        default=...,
        example={
            "name": "Updated Smartphone",
            "description": "Latest model with even better features",
            "price": 899.99,
            "tax": 89.99,
            "category": "electronics",
        },
    ),
) -> Item:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not. found")

    updated_item: Item = Item(id=item_id, **item.model_dump())
    items_db[item_id] = updated_item
    return updated_item


@app.delete(path="/items/{item_id}", status_code=204)
def delete_item(item_id: int = Path(default=..., gt=0)) -> None:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not. found")

    del items_db[item_id]
    return None
