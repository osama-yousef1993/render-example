from fastapi import FastAPI
from pydantic import BaseModel

fixture_orders = [
    {
        "product": "Cloak of invisibility",
        "quantity": 1,
    },
    {
        "product": "Deluminator",
        "quantity": 1,
    },
]


server = FastAPI()


class PlaceOrderSchema(BaseModel):
    product: str
    quantity: int


class GetOrderSchema(PlaceOrderSchema):
    id: int


class ListOrdersSchema(BaseModel):
    orders: list[GetOrderSchema]


@server.get("/orders", response_model=ListOrdersSchema)
def list_orders():
    orders = list()
    for order in fixture_orders:
        orders.append(
            {
                "id": len(orders) + 1,
                "product": order["product"],
                "quantity": order["quantity"],
            }
        )

    return {"orders": list(orders)}
