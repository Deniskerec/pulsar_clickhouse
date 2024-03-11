from pulsar import Client
from clickhouse_driver import Client as CHClient

# Pulsar Configuration
pulsar_client = Client('pulsar://localhost:6650')
topic = 'persistent://public/default/my-topic'

# ClickHouse Configuration
ch_client = CHClient(host='localhost')
db_name = 'default'
table_name = 'test_denis'

# Step 1: Create a table in ClickHouse
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {db_name}.{table_name} (
    id UInt64,
    message String
) ENGINE = MergeTree()
ORDER BY id
"""

ch_client.execute(create_table_query)

# Step 2: Generate and Send Messages to Pulsar
producer = pulsar_client.create_producer(topic)
for i in range(10):  # Example: Send 10 messages
    message = f"Message {i}"
    producer.send((f"{i},{message}").encode('utf-8'))

# Assuming direct insertion to ClickHouse, simulate consuming the message
for i in range(10):
    message = f"old_msg {i}"
    insert_query = f"INSERT INTO {db_name}.{table_name} (id, message) VALUES"
    ch_client.execute(f"{insert_query} ({i}, '{message}')")

# Cleanup
producer.close()
pulsar_client.close()