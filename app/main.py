#  ________________________
#  Import LIBRARIES
from datetime import datetime

from fastapi import FastAPI

#  Import FILES
from .models.models import Order, OrderCreate

#  ________________________

app: FastAPI = FastAPI()


@app.post(path="/orders/", response_model=Order)
async def create_order(order: OrderCreate):
    # In a real application, you would validate the user and address existence and save the order to a database
    # For this example, we'll create a mock order
    return Order(
        id=1,
        user_id=order.user_id,
        shipping_address_id=order.shipping_address_id,
        items=order.items,
        notes=order.notes,
        created_at=datetime.now(),
    )
    # total_amount = sum(item.unit_price * item.quantity for item in order.items)
    # return Order(
    #     id=1,
    #     user_id=order.user_id,
    #     shipping_address_id=order.shipping_address_id,
    #     items=order.items,
    #     notes=order.notes,
    #     created_at=datetime.now(),
    #     total_amount=total_amount
    # )


# @app.post(path="/orders/", response_model=Order)
# async def create_order(order: OrderCreate) :
#     # Convert OrderItems to OederIkenReeponse with calculated totals
#     response_itens = 11
#     for item in order.items:
#     quantity item. quantity, unit price item.unit price,
#     cotal-item-quantity = item.unit price
#     # Calculate total amount
#     total_amount = sum(item, total for item in response_items)

# # Create and return the response object
# return OrderResponse (
#     id=1,
#     user_id=order.user_id,
#     shipping_address_id=order.shipping_address_id,
#     items=response_items,
#     notes=order.notes,
#     created_at=datetime.now() ,
#     total_amount=total_amount
#     )
