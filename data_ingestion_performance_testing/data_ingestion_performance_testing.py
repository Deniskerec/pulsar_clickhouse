import pulsar
import time
import json
from clickhouse_driver import Client as CHClient, errors as CHErrors

def create_clickhouse_database_and_table(host='localhost'):
    try:
        client = CHClient(host=host)
        database_name = 'performance_database'
        client.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        client = CHClient(host=host, database=database_name)
        client.execute("""
            CREATE TABLE IF NOT EXISTS pulsar_messages (
                ID Int64,
                Timestamp DateTime,
                Data1 Int32,
                Data2 Int32,
                JSONData String
            ) ENGINE = MergeTree()
            ORDER BY ID
            """)
        print(f"Database '{database_name}' and table 'pulsar_messages' are ready.")
    except CHErrors.ServerException as e:
        print(f"Failed to create database or table in ClickHouse: {e}")
        exit(1)

def generate_message(id):
    message = {
        "ID": id,
        "Timestamp": int(time.time()),
        "Data1": id * 5,
        "Data2": id + 100,
        "JSONData": json.dumps({"key": "value", "id": id})
    }
    return json.dumps(message)

def produce_messages(client_url, topic, message_count):
    try:
        client = pulsar.Client(client_url)
        producer = client.create_producer(topic)
        
        start_time = time.time()
        for i in range(message_count):
            message = generate_message(i+1)
            producer.send(message.encode('utf-8'))
            print(f"Sent: {message}")
        
        duration = time.time() - start_time
        print(f"Finished sending {message_count} messages in {duration:.2f} seconds.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        producer.close()
        client.close()

if __name__ == "__main__":
    clickhouse_host = 'localhost'
    create_clickhouse_database_and_table(host=clickhouse_host)
    
    client_url = 'pulsar://localhost:6650'
    topic = 'persistent://public/default/my-topic'
    message_count = int(input("number of msg.: "))
    
    produce_messages(client_url, topic, message_count)
