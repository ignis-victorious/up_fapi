#  ________________________
#  Import LIBRARIES
import json
from datetime import datetime
from typing import NewType

from fastapi import FastAPI

#  Import FILES
from .models.models import Article, Product, User, UserCreate, UserResponse

#  ________________________


app: FastAPI = FastAPI()


#   Lecture 4
#  Basic Model
# Valid data
user: User = User(id=1, name="John Doe", email="john@example.com")
print(user.model_dump())

# Invalid data raises ValidationError
# try:
#     User(id="not-an-integer", name=123, email="invalid-email")
# except Exception as e:
#     print(f"Validation error: {e}")


# Basic Validation with Type Annotations
try:
    product: Product = Product(
        id=1,
        name="Erre",
        price=99.99,
        description="This is a description",
        contact_email="erre@email.com",
        # quantity=10,
        quantity=10,
    )
    print(product.model_dump())
except Exception as e:
    print(f"Validation error: {e}")

# try:
#     signup_form = SignupForm(username="Elle", password1="my_pass", password2="my_pass")
#     print(signup_form.model_dump())
# except Exception as e:
#     print(f"Validation error: {e}")


# Create a model from Python objects
article: Article = Article(
    id=1,
    title="Pydantic V2 is Amazing",
    content="This is the content of the article.",
    published=datetime.now(),
    tags=["pydantic", "python", "fastapi"],
)

# Serialize to JSON
json_data: str = article.model_dump_json()
print(json_data)

# Deserialize from JSON
article_dict = json.loads(s=json_data)
# Need to manually parse datetime when deserializing from raw JSON
article_dict["published"] = datetime.fromisoformat(article_dict["published"])
new_article: Article = Article.model_validate(obj=article_dict)


@app.post(path="/users/", response_model=UserResponse)
async def create_user(user: UserCreate) -> UserResponse:
    # FastAPI automatically validates user data based on the Pydantic model
    # If validation fails, it returns a 422 Unprocessable Entity error
    # Here you would typically save the user to a database
    # For this example, we'll just return a mock response
    return UserResponse(id=1, username=user.username, email=user.email)


# Custom Data Types

# Option 1: Using NewType with Pydantic validators
UserId = NewType("UserId", str)

# Option 2: Using Annotated with Field constraints
ISBN = Annotated[
    str, Field(pattern=r"^ (?=(?: \D*\d) {10} (?: (?: \D*\d) (3)) 29) [\d-] +$")
]
