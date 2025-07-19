#  ________________________
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from .models.models import Item

#  ________________________


# # Create an instance of the FastAPI class
# app: FastAPI = FastAPI()

# Create an instance with metadata
app: FastAPI = FastAPI(
    title="My First API",
    description="A simple API built with FastAPI",
    version="0.1.0",
    docs_url="/documentation",  # Change the docs URL
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


# Define a path + query parameter endpoint - Works with: http://127.0.0.1:8000/items/123?q=erre
@app.get(path="/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict[str, int | str | None]:
    return {"item_id": item_id, "q": q}


# Define a POST endpoint with request body - Works with _ {"name": "Laptop", "price": 10, "is_offer": false}
@app.post(path="/items/")
def create_item(item: Item) -> Item:
    return item


# def main():
#     print("Hello from up-fapi!")


# if __name__ == "__main__":
#     main()
