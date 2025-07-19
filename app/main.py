#  ________________________
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
#  ________________________


# Create an instance of the FastAPI class
app: FastAPI = FastAPI()


# Define a root endpoint
@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}


# Define a path parameter endpoint
@app.get(path="/items/{item_id}")
def read_item(item_id: int) -> dict[str, int]:
    return {"item_id": item_id}


# def main():
#     print("Hello from up-fapi!")


# if __name__ == "__main__":
#     main()
