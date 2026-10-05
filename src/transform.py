"""
Transform module.

Cleans and prepares extracted data before loading it
into PostgreSQL.
"""

import pandas as pd


def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    """Clean customer data."""
    result = df.copy()

    result["name"] = result["name"].str.strip()
    result["email"] = result["email"].str.strip().str.lower()
    result["country"] = result["country"].str.strip()

    return result


def transform_products(df: pd.DataFrame) -> pd.DataFrame:
    """Clean product data."""
    result = df.copy()

    result["product_name"] = result["product_name"].str.strip()
    result["category"] = result["category"].str.strip()
    result["price"] = pd.to_numeric(
        result["price"],
        errors="coerce",
    )

    return result


def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Clean order data."""
    result = df.copy()

    result["order_date"] = pd.to_datetime(
        result["order_date"],
        errors="coerce",
    )

    result["quantity"] = pd.to_numeric(
        result["quantity"],
        errors="coerce",
    ).astype("Int64")

    return result
