# python-postgresql-etl
# Python PostgreSQL ETL Pipeline

A production-style ETL pipeline built with Python and PostgreSQL for extracting, validating, transforming, and loading structured business data.

## Overview

This project demonstrates how to build a reliable data pipeline using Python and PostgreSQL.

The pipeline processes customer, product, and order data from CSV files and loads the cleaned data into PostgreSQL.

## ETL Flow

CSV Files
   ↓
Extract
   ↓
Validate
   ↓
Transform
   ↓
Load
   ↓
PostgreSQL
   ↓
SQL Reports

## Technologies

- Python
- PostgreSQL
- SQL
- Pandas
- Pytest
- Docker

## Key Features

- CSV data ingestion
- Data validation
- Data transformation
- Duplicate detection
- PostgreSQL database loading
- Batch processing
- Error handling
- Logging
- Unit testing
- SQL reporting
- Docker support

## Project Structure

```text
python-postgresql-etl/
│
├── src/
├── tests/
├── sample_data/
├── sql/
├── requirements.txt
└── README.md
