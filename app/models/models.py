#  ________________________
#  Import LIBRARIES
# from pydantic import BaseModel, Field, Emailstr, model_validator
from datetime import datetime

from pydantic import BaseModel, Field, model_validator

#  Import FILES
#  ________________________


# class Address(BaseModel):
#     street: str
#     city: str
#     state: str
#     zip_code: str
#     country: str


# class User(BaseModel):
#     id: int
#     name: str
#     email: str
#     address: Address


# # Example use
# user: User = User(
#     id=1,
#     name="John Doe",
#     email="john@example.com",
#     address=Address(
#         street="123 Main St",
#         city="Anytown",
#         state="CA",
#         zip_code="12345",
#         country="USA",
#     ),
# )

# print("User: ")
# print(user.model_dump_json())


class Tag(BaseModel):
    id: int
    name: str


class Post(BaseModel):
    id: int
    title: str
    content: str
    tags: list[Tag] = []


# Example
post: Post = Post(
    id=1,
    title="Hello World",
    content="This is my first post",
    tags=[
        Tag(id=1, name="python"),
        Tag(id=2, name="pydantic"),
        Tag(id=3, name="fastapi"),
    ],
)

print("Post: ")
print(post.model_dump_json())


class Comment(BaseModel):
    id: int
    text: str
    replies: list["Comment"] = []


Comment.model_rebuild()  # Required in Pydantic V2 for recursive models


# Example
comment: Comment = Comment(
    id=1,
    text="Great article!",
    replies=[
        Comment(id=2, text="Thanks!"),
        Comment(id=3, text="I agree!", replies=[Comment(id=4, text="Me too!")]),
    ],
)

print("Comment: ")
print(comment.model_dump_json())


#  ORDER
class AddressCreate(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    country: str


class Address(AddressCreate):
    id: int


class OrderItem(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)

    @model_validator(mode="after")
    def calculate_total(self) -> "OrderItem":
        self.total: float = self.quantity * self.unit_price
        return self


class OrderCreate(BaseModel):
    user_id: int
    shipping_address_id: int
    items: list[OrderItem]
    notes: str | None = None


class Order(OrderCreate):
    id: int
    created_at: datetime = datetime.now()
    total_amount: float

    @model_validator(mode="after")
    def calculate_total_amount(self) -> "Order":
        self.total_amount = sum(item.quantity * item.unit_price for item in self.items)
        return self


# {
#     "user_id": 1,
#     "shipping_address_id": 1,
#     "items": [{"product_id": 1, "quantity": 10, "unit_price": 1.99}],
#     "notes": "This is a note",
# }

# class OrdeResponse(BaseModel):
#     id: int
#     user_id: int
#     shipping_address_id: int
#     items:  list[OrdeRItemResponse]
#     notes: str|None = None
#     created_at: datetime
#     total_amount: float
