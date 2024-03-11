from pulsar import Client
import time
import json
from clickhouse_driver import Client as CHClient, errors as CHErrors

def db():
    try:
        ch_client = CHClient(host='localhost')
        db_name = 'performance_database'
        table_name = 'pulsar_messages'
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {db_name}.{table_name} (
            ID Int64,
            Timestamp DateTime,
            Data1 Int32,
            Data2 Int32,
            JSONData String
        ) ENGINE = MergeTree()
        ORDER BY ID
        """
        ch_client.execute(create_table_query)
        print(f"Table {db_name}.{table_name} created for direct data inserts.")
        return ch_client, db_name, table_name
    except CHErrors.Error as e:
        print(f"ClickHouse error: {e}")
        return None, None, None

def pulsar(ch_client, db_name, table_name, pulsar_client, topic):
    producer = None
    try:
        producer = pulsar_client.create_producer(topic)
        print("Producer created successfully.")
    except Exception as e:
        print(f"Failed to create Pulsar producer: {e}")
        return

    start_time = time.time()  
    
    try:
        for i in range(3000):  #number of insertions
            message_data = {
                "ID": i,
                "Timestamp": int(time.time()),
                "Data1": i * 5,
                "Data2": i + 100,
                "JSONData": json.dumps({"key": "value", "id": i})
            }
            message_json = json.dumps(message_data)
            producer.send(message_json.encode('utf-8'))
            
            # direct insert into clickhouse
            insert_query = f"""
            INSERT INTO {db_name}.{table_name} (ID, Timestamp, Data1, Data2, JSONData)
            VALUES ({i}, {message_data["Timestamp"]}, {message_data["Data1"]}, {message_data["Data2"]}, '{message_data["JSONData"]}')
            """
            ch_client.execute(insert_query)
            
    except Exception as e:
        print(f"Error sending message to Pulsar or inserting into ClickHouse: {e}")
    finally:
        if producer:
            producer.close()
            pulsar_client.close()

    end_time = time.time()  
    print(f"Finished sending messages and inserting into ClickHouse in {end_time - start_time:.2f} seconds.")

if __name__ == '__main__':
    pulsar_client = Client('pulsar://localhost:6650')
    topic = 'persistent://public/default/my-topic'
    ch_client, db_name, table_name = db()
    if ch_client is not None and db_name is not None and table_name is not None:
        pulsar(ch_client, db_name, table_name, pulsar_client, topic)
    else:
        print("Database initialization failed, exiting.")
