import psycopg2

# Connect to the remote PostgreSQL database
remote_conn = psycopg2.connect(
    dbname="remote_dbname",
    user="remote_user",
    password="remote_password",
    host="remote_host"
)

# Connect to your local/own PostgreSQL database
local_conn = psycopg2.connect(
    dbname="local_dbname",
    user="local_user",
    password="local_password",
    host="local_host"
)

remote_cur = remote_conn.cursor()
local_cur = local_conn.cursor()

# Example query to fetch data from the remote database
remote_cur.execute("SELECT * FROM remote_table")

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
