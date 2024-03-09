from pulsar import Client
from clickhouse_driver import Client as CHClient, errors as ch_errors

def db():
    try:
        ch_client = CHClient(host='localhost')
        db_name = 'default'
        table_name = 'test_denis'
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {db_name}.{table_name} (
            id UInt64,
            message String
        ) ENGINE = MergeTree()
        ORDER BY id
        """
        ch_client.execute(create_table_query)
        return ch_client, db_name, table_name
    except ch_errors.Error as e:
        print(f"ClickHouse error: {e}")
        return None, None, None

def pulsar(ch_client, db_name, table_name, pulsar_client, topic):
    try:
        producer = pulsar_client.create_producer(topic)
    except Exception as e:  # Generalized exception handling
        print(f"Failed to create Pulsar producer: {e}")
        return

    try:
        for i in range(10, 30):  # Adjusted to send 20 messages for demonstration
            message = f"Test {i}"
            producer.send((f"{i},{message}").encode('utf-8'))
    except Exception as e:
        print(f"Failed to send message to Pulsar: {e}")

    try:
        for i in range(10, 30):
            message = f"debus {i}"
            insert_query = f"INSERT INTO {db_name}.{table_name} (id, message) VALUES"
            ch_client.execute(f"{insert_query} ({i}, '{message}')")
    except ch_errors.Error as e:
        print(f"ClickHouse insert error: {e}")
    except Exception as e:
        print(f"Unexpected error when inserting into ClickHouse: {e}")
    finally:
        if producer:
            producer.close()
            pulsar_client.close()

if __name__ == '__main__':
    pulsar_client = Client('pulsar://localhost:6650')
    topic = 'persistent://public/default/my-topic'
    ch_client, db_name, table_name = db()
    if ch_client is not None and db_name is not None and table_name is not None:
        pulsar(ch_client, db_name, table_name, pulsar_client, topic)
    else:
        print("Database initialization failed, exiting.")
