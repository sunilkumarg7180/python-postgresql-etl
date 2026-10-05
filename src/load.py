"""
Load module.

Loads transformed data into PostgreSQL.
"""

import os

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values


def get_connection():
    """Create a PostgreSQL database connection."""
    return psycopg2.connect(
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", "5432"),
        database=os.getenv("PGDATABASE", "etl_demo"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD"),
    )


def load_customers(df: pd.DataFrame, connection) -> None:
    """Load customer records into PostgreSQL."""
    query = """
        INSERT INTO customers (
            customer_id,
            name,
            email,
            country
        )
        VALUES %s
        ON CONFLICT (customer_id)
        DO UPDATE SET
            name = EXCLUDED.name,
            email = EXCLUDED.email,
            country = EXCLUDED.country;
    """

    records = [
        (
            int(row.customer_id),
            row.name,
            row.email,
            row.country,
        )
        for row in df.itertuples(index=False)
    ]

    with connection.cursor() as cursor:
        execute_values(cursor, query, records)

    connection.commit()


def load_products(df: pd.DataFrame, connection) -> None:
    """Load product records into PostgreSQL."""
    query = """
        INSERT INTO products (
            product_id,
            product_name,
            category,
            price
        )
        VALUES %s
        ON CONFLICT (product_id)
        DO UPDATE SET
            product_name = EXCLUDED.product_name,
            category = EXCLUDED.category,
            price = EXCLUDED.price;
    """

    records = [
        (
            int(row.product_id),
            row.product_name,
            row.category,
            float(row.price),
        )
        for row in df.itertuples(index=False)
    ]

    with connection.cursor() as cursor:
        execute_values(cursor, query, records)

    connection.commit()


def load_orders(df: pd.DataFrame, connection) -> None:
    """Load order records into PostgreSQL."""
    query = """
        INSERT INTO orders (
            order_id,
            customer_id,
            product_id,
            quantity,
            order_date
        )
        VALUES %s
        ON CONFLICT (order_id)
        DO UPDATE SET
            customer_id = EXCLUDED.customer_id,
            product_id = EXCLUDED.product_id,
            quantity = EXCLUDED.quantity,
            order_date = EXCLUDED.order_date;
    """

    records = [
        (
            int(row.order_id),
            int(row.customer_id),
            int(row.product_id),
            int(row.quantity),
            row.order_date.date(),
        )
        for row in df.itertuples(index=False)
    ]

    with connection.cursor() as cursor:
        execute_values(cursor, query, records)

    connection.commit()
