#  ________________________
#  Import LIBRARIES
from datetime import date

from fastapi import FastAPI, Path, Query

#  Import FILES
from .models.models import Item, ModelName

#  ________________________


# # Create an instance of the FastAPI class
# app: FastAPI = FastAPI()

# Create an instance with metadata
app: FastAPI = FastAPI(
    title="My First API",
    description="A simple API built with FastAPI",
    version="0.1.0",
    docs_url="/documentation",  # Change the docs URL !!!
    redoc_url="/redoc",
)


# Define a root endpoint.
@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}


# # Define a path parameter endpoint.
# @app.get(path="/items/{item_id}")
# def read_item(item_id: int) -> dict[str, int]:
#     return {"item_id": item_id}


# # Define a path + query parameter endpoint - Works with: http://127.0.0.1:8000/items/123?q=erre
# @app.get(path="/items/{item_id}")
# def read_item(item_id: int, q: str | None = None) -> dict[str, int | str | None]:
#     return {"item_id": item_id, "q": q}


# Define a POST endpoint with request body - Works with _ {"name": "Laptop", "price": 10, "is_offer": false}
@app.post(path="/items/")
def create_item(item: Item) -> Item:
    return item


# Works with: http://127.0.0.1:8000/items/123 (but not with 12345678)
@app.get(path="/items/{item_id}")
def read_item(
    item_id: int = Path(default=..., title="The ID of the item", ge=0, le=1000),
) -> dict[str, int]:  # With Path Parameter Validation
    return {"item_id": item_id}


# Multiple Values for the Same Parameter - Works with: http://127.0.0.1:8000/items/?q=erre&q=esse&q=emme
@app.get(path="/items/")
def read_items(q: list[str] = Query(default=None)) -> dict[str, list[str]]:
    return {"q": q}


# #  Boolean Type Conversion
# @app.get(path="/items/")
# def read_items(featured: bool = False) -> dict[str, str]:
#     if featured:
#         return {"featured": "Get only featured items"}
#     return {"featured": "Get all items"}


# #  Works with: http://127.0.0.1:8000/items/?q=aaa but not with ?q=aa or ?q=a1a or ...
# @app.get(path="/items/")
# def read_items(
#     q: str | None = Query(
#         default=None,  # Default value
#         min_length=3,  # Minimum length
#         max_length=50,  # Maximum length
#         regex="^[a-z]+$",  # Regular expression pattern
#         title="Query string",  # Title for documentationdescription="Query string for filtering items" # Description for does
#     ),
# ) -> dict[str, list[dict[str, str]]]:
#     results: dict[str, list[dict[str, str]]] = {
#         "items": [{"item_id": "Foo"}, {"item_id": "Bar"}]
#     }
#     if q:
#         # results.update({"q": q})
#         results["items"].append({"item_id": q})
#     return results


#  Works with: http://127.0.0.1:8000/items/?required_query=erre and http://127.0.0.1:8000/items/?required_query=erre&optional_query=esse
# @app.get(path="/items/")
# def read_items(
#     required_query: str,  # Required parameter (no default value)
#     optional_query: str | None = None,  # Optional parameter
# ) -> dict[str, str]:
#     results: dict[str, str] = {"required": required_query}
#     if optional_query:
#         results.update({"optional": optional_query})
#     return results


# #  Query Parameters - Worls with: http://127.0.0.1:8000/items/?skip=20&limit=50
# @app.get(path="/items/")
# def read_items(skip: int = 0, limit: int = 10) -> dict[str, int]:
#     return {"skip": skip, "limit": limit}


# # Works with: http://127.0.0.1:8000/items/12345678
# @app.get(path="/items/{item_id}")
# def read_item(item_id: int) -> dict[str, int]:  # Integer validation
#     return {"item_id": item_id}


# Works with: http://127.0.0.1:8000/users/user1
@app.get(path="/users/{user_id}")
def read_user(user_id: str) -> dict[str, str]:  # String (default)
    return {"user_id": user_id}


#  Works with: http://127.0.0.1:8000/files/{file_path:path)?file_path=folder%2Ffolder%2Ffile
@app.get(path="/files/{file_path:path)")
def read_file(file_path: str) -> dict[str, str]:  # Path parameter containing slashes
    return {"file_path": file_path}


#  Predefined Values with Enum
@app.get(path="/models/{model_name}")
def get_model(model_name: ModelName) -> dict[str, ModelName | str]:
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


# #  Works with: http://127.0.0.1:8000/models/497f6eca-6276-4993-bfeb-53cbbbba6f08
# @app.get(path="/models/{model_uuid}")
# def get_model(model_uuid: UUID) -> dict[str, UUID]:  # UUID validation
#     print(f"model uiid: {model_uuid}")
#     return {"model_uuid": model_uuid}


#  This works: http://127.0.0.1:8000/events/2025-01-01
@app.get(path="/events/{event_date}")
def get_events(event_date: date) -> dict[str, date]:  # Date validation (YYYY-MM-DD)
    return {"event_date": event_date}


# def main():
#     print("Hello from up-fapi!")


# if __name__ == "__main__":
#     main()
