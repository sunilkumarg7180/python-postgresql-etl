import pandas as pd

from src.transform import (
    transform_customers,
    transform_orders,
    transform_products,
)


def test_transform_customers():
    data = pd.DataFrame(
        {
            "customer_id": [1],
            "name": ["  Ravi Kumar  "],
            "email": [" RAVI@EXAMPLE.COM "],
            "country": [" India "],
        }
    )

    result = transform_customers(data)

    assert result.loc[0, "name"] == "Ravi Kumar"
    assert result.loc[0, "email"] == "ravi@example.com"
    assert result.loc[0, "country"] == "India"


def test_transform_products():
    data = pd.DataFrame(
        {
            "product_id": [101],
            "product_name": [" Laptop "],
            "category": [" Electronics "],
            "price": ["75000"],
        }
    )

    result = transform_products(data)

    assert result.loc[0, "product_name"] == "Laptop"
    assert result.loc[0, "category"] == "Electronics"
    assert result.loc[0, "price"] == 75000


def test_transform_orders():
    data = pd.DataFrame(
        {
            "order_id": [1001],
            "customer_id": [1],
            "product_id": [101],
            "quantity": ["2"],
            "order_date": ["2026-09-01"],
        }
    )

    result = transform_orders(data)

    assert result.loc[0, "quantity"] == 2
    assert str(result.loc[0, "order_date"].date()) == "2026-09-01"
