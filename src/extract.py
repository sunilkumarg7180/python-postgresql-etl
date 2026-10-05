"""
Extract module.

Reads CSV files from the sample_data directory.
"""

from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).resolve().parent.parent / "sample_data"


def extract_customers():
    """Read customer data from CSV."""
    file_path = DATA_DIR / "customers.csv"
    return pd.read_csv(file_path)


def extract_products():
    """Read product data from CSV."""
    file_path = DATA_DIR / "products.csv"
    return pd.read_csv(file_path)


def extract_orders():
    """Read order data from CSV."""
    file_path = DATA_DIR / "orders.csv"
    return pd.read_csv(file_path)
