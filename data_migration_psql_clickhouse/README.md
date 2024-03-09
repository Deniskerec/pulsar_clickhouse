# PostgreSQL to ClickHouse Data Migration

This script facilitates the migration of data from a PostgreSQL database to a ClickHouse database. It is designed to ensure accurate and efficient transfer of data from specific tables.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Configuration](#configuration)
- [Running the Script](#running-the-script)
- [Monitoring Migration Duration](#monitoring-migration-duration)

## Features

- Fetches data from the PostgreSQL `afct_financial_table`.
- Transforms data to comply with ClickHouse schema requirements, if necessary.
- Inserts data into the corresponding ClickHouse `afct_financial_table`.
- Implements basic error handling for common migration issues.
- Reports the time duration of the migration process.

## Prerequisites

- Python 3.6 or newer.
- Installation of `psycopg2` and `clickhouse-driver` Python libraries. Install these using pip:

  ```sh
  pip install psycopg2-binary clickhouse-driver
  ```

- Access to the PostgreSQL database with permissions to read the data.
- Access to the ClickHouse database with permissions to create tables and insert data.

## Configuration

Configure the database connection parameters within the script for both PostgreSQL and ClickHouse:

- **PostgreSQL Connection Parameters (`pg_params`):**

  ```python
  pg_params = {
      "dbname": "your_postgres_db_name",
      "user": "your_postgres_user",
      "password": "your_postgres_password",
      "host": "your_postgres_host"
  }
  ```

- **ClickHouse Connection Parameters (`ch_params`):**

  ```python
  ch_params = {
      "host": "your_clickhouse_host",
      "port": 9000,  
      "database": "your_clickhouse_db_name"
  }
  ```

Modify these parameters to match your specific database configurations.

## Running the Script

Execute the script by navigating to its directory and running:

```sh
python3 path_to_your_script.py
```

Replace `path_to_your_script.py` with the actual path to your migration script.

## Monitoring Migration Duration

The script prints the total duration of the migration process upon successful completion, allowing you to monitor the performance of the data transfer.

