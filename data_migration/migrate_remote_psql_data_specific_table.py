import psycopg2
from db_info import remote_con_info

# remote PostgreSQL database
#    ├── db_info/
#    │   └── remote_con_info.py
remote_conn = psycopg2.connect(
    dbname=remote_con_info.DB_NAME,
    user=remote_con_info.USER,
    password=remote_con_info.PASSWORD,
    host=remote_con_info.HOST
)

# local PostgreSQL database

local_conn = psycopg2.connect(
    dbname="postgres_migration",
    user="pulsar",
    password="pulsar",
    host="localhost"
    #port = if custom port add here.
)

remote_cur = remote_conn.cursor()
local_cur = local_conn.cursor()

# Example query to fetch data from the remote database
remote_cur.execute("SELECT * FROM afct_financial_table aft")

# Fetch all data
rows = remote_cur.fetchall()

# Example query to insert data into your own database
# Ensure the schema of 'local_table' matches the data being inserted
for row in rows:
    local_cur.execute(
        "INSERT INTO local_table VALUES (%s, %s, ...)", row
    )

local_conn.commit()

# Close connections
remote_cur.close()
local_cur.close()
remote_conn.close()
local_conn.close()



