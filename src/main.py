"""
Main ETL pipeline.

Runs the complete Extract -> Transform -> Validate -> Load workflow.
"""

from extract import (
    extract_customers,
    extract_orders,
    extract_products,
)
from load import (
    get_connection,
    load_customers,
    load_orders,
    load_products,
)
from transform import (
    transform_customers,
    transform_orders,
    transform_products,
)
from validate import (
    validate_customers,
    validate_orders,
    validate_products,
)


def run_pipeline():
    """Run the complete ETL pipeline."""

    print("Starting ETL pipeline...")

    # 1. Extract
    print("Extracting data...")

    customers = extract_customers()
    products = extract_products()
    orders = extract_orders()

    # 2. Transform
    print("Transforming data...")

    customers = transform_customers(customers)
    products = transform_products(products)
    orders = transform_orders(orders)

    # 3. Validate
    print("Validating data...")

    validate_customers(customers)
    validate_products(products)
    validate_orders(orders)

    # 4. Load
    print("Loading data into PostgreSQL...")

    connection = get_connection()

    try:
        load_customers(customers, connection)
        load_products(products, connection)
        load_orders(orders, connection)

        print("ETL pipeline completed successfully.")

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


if __name__ == "__main__":
    run_pipeline()
