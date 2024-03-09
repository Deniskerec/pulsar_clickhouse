import psycopg2
from clickhouse_driver import Client
import time


# PostgreSQL 
pg_params = {
    "dbname": "afc_restored_database",
    "user": "pulsar",
    "password": "pulsar",
    "host": "localhost"
}

# ClickHouse 
ch_params = {
    "host": "localhost",
    "port": 9000,
    "database": "hafil_dev_afc"
}

def fetch_data_from_postgres():
    """Fetch data directly from PostgreSQL."""
    with psycopg2.connect(**pg_params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM afct_financial_table")
            data = cur.fetchall()
    return data

def load_data_into_clickhouse(data):
    """Load data into ClickHouse."""
    client = Client(**ch_params)
    insert_query = 'INSERT INTO afct_financial_table VALUES'
    client.execute(insert_query, data)

if __name__ == "__main__":
    start_time = time.time()  
    
    data = fetch_data_from_postgres()
    if data:
        load_data_into_clickhouse(data)
        end_time = time.time()  
        duration = end_time - start_time  
        print(f"Data migration completed successfully in {duration:.2f} seconds.")
    else:
        print("Data migration failed.")
