"""
Validation module.

Contains data quality checks for ETL input data.
"""

import pandas as pd


def validate_customers(df: pd.DataFrame) -> None:
    """Validate customer data."""
    required_columns = {
        "customer_id",
        "name",
        "email",
        "country",
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing customer columns: {missing_columns}"
        )

    if df["customer_id"].isnull().any():
        raise ValueError("Customer ID contains NULL values.")

    if df["customer_id"].duplicated().any():
        raise ValueError("Duplicate customer IDs found.")


def validate_products(df: pd.DataFrame) -> None:
    """Validate product data."""
    required_columns = {
        "product_id",
        "product_name",
        "category",
        "price",
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing product columns: {missing_columns}"
        )

    if df["product_id"].duplicated().any():
        raise ValueError("Duplicate product IDs found.")

    if (df["price"] < 0).any():
        raise ValueError("Product price cannot be negative.")


def validate_orders(df: pd.DataFrame) -> None:
    """Validate order data."""
    required_columns = {
        "order_id",
        "customer_id",
        "product_id",
        "quantity",
        "order_date",
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing order columns: {missing_columns}"
        )

    if df["order_id"].duplicated().any():
        raise ValueError("Duplicate order IDs found.")

    if (df["quantity"] <= 0).any():
        raise ValueError("Order quantity must be greater than zero.")
