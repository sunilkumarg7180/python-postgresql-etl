import pandas as pd
import pytest

from src.validate import (
    validate_customers,
    validate_products,
    validate_orders,
)


def test_validate_customers_duplicate_id():
    data = pd.DataFrame(
        {
            "customer_id": [1, 1],
            "name": ["Ravi Kumar", "John Smith"],
            "email": ["ravi@example.com", "john@example.com"],
            "country": ["India", "USA"],
        }
    )

    with pytest.raises(ValueError, match="Duplicate customer IDs found."):
        validate_customers(data)


def test_validate_products_negative_price():
    data = pd.DataFrame(
        {
            "product_id": [101],
            "product_name": ["Laptop"],
            "category": ["Electronics"],
            "price": [-100],
        }
    )

    with pytest.raises(ValueError, match="Product price cannot be negative."):
        validate_products(data)


def test_validate_orders_invalid_quantity():
    data = pd.DataFrame(
        {
            "order_id": [1001],
            "customer_id": [1],
            "product_id": [101],
            "quantity": [0],
            "order_date": ["2026-09-01"],
        }
    )

    with pytest.raises(
        ValueError,
        match="Order quantity must be greater than zero.",
    ):
        validate_orders(data)
