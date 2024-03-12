from pulsar import Client
import json
import time

def produce_messages_to_pulsar(pulsar_url, topic_name, num_messages):
    """
    Produces messages to a specified Pulsar topic.
    :param pulsar_url: URL for the Pulsar instance.
    :param topic_name: Name of the Pulsar topic to produce messages to.
    :param num_messages: Number of messages to produce.
    """
    client = Client(pulsar_url)
    producer = client.create_producer(topic_name)

    for i in range(num_messages):
        message = {
            "ID": i,
            "Timestamp": int(time.time()),
            "Data1": i * 5,
            "Data2": i + 100,
            "JSONData": json.dumps({"key": "value", "id": i})
        }
        producer.send(json.dumps(message).encode('utf-8'))
        print(f"Sent message {i}")

    producer.close()
    client.close()

if __name__ == "__main__":
    pulsar_url = 'pulsar://localhost:6650'  
    topic_name = 'persistent://public/default/my-topic'  
    num_messages = 100  
    produce_messages_to_pulsar(pulsar_url, topic_name, num_messages)
