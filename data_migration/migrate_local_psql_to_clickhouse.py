from clickhouse_driver import Client as CHClient
import psycopg2

# Connect to your PostgreSQL database
local_conn = psycopg2.connect(
    dbname="local_dbname",
    user="local_user",
    password="local_password",
    host="local_host"
)

# Connect to ClickHouse
ch_client = CHClient(host='clickhouse_host')

local_cur = local_conn.cursor()

# Query to fetch data from your own database
local_cur.execute("SELECT * FROM local_table")

rows = local_cur.fetchall()

# Insert fetched data into ClickHouse
for row in rows:
    ch_client.execute(
        "INSERT INTO clickhouse_table VALUES", [row]
    )

# Close connections
local_cur.close()
local_conn.close()
