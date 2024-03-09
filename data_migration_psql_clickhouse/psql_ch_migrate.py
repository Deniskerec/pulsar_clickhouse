import psycopg2
from clickhouse_driver import Client

# PostgreSQL connection parameters
pg_params = {
    "dbname": "afc_restored_database",
    "user": "pulsar",
    "password": "pulsar",
    "host": "localhost"
}

# ClickHouse connection parameters
ch_params = {
    "host": "localhost",
    "port": 9000,
    "user": "default",  # Default user for ClickHouse
    "password": "",
    "database": "hafil_dev_afc"
}

# Define your complex SQL query (simplified version)
sql_query = '''
SELECT * FROM afct_financial_table;
'''

def fetch_data_from_postgres():
    """Fetch data based on the complex SQL query from PostgreSQL."""
    with psycopg2.connect(**pg_params) as conn:
        with conn.cursor() as cur:
            cur.execute(sql_query)
            data = cur.fetchall()
    return data

#def transform_data(data):
 #   """Transform data if necessary (this step is optional and based on your needs)."""
    # This is where you would adjust data formats or perform transformations
    # For simplicity, this example does not perform any transformations
  #  return data

def load_data_into_clickhouse(data):
    """Load transformed data into ClickHouse."""
    client = Client(**ch_params)
    
    insert_query = '''
    INSERT INTO afct_financial_table VALUES
    '''
    
    client.execute(insert_query, data)

if __name__ == "__main__":
    data = fetch_data_from_postgres()
    transformed_data = transform_data(data)
    load_data_into_clickhouse(transformed_data)
    print("Data migration completed.")
