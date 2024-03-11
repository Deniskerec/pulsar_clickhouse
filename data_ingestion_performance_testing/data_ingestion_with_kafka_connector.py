from confluent_kafka import Producer
import json
import time

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def produce_messages(producer_config, topic, num_messages=5000):
    producer = Producer(**producer_config)
    
    for i in range(num_messages):
        message_data = {
            "ID": i,
            "Timestamp": int(time.time()),
            "Data1": i * 5,
            "Data2": i + 100,
            "JSONData": json.dumps({"key": "value", "id": i})
        }
        producer.produce(topic, json.dumps(message_data).encode('utf-8'), callback=delivery_report)
        producer.poll(0)
    
    producer.flush()
    print(f"Finished sending {num_messages} messages to topic {topic}.")

if __name__ == '__main__':
    producer_config = {
        'bootstrap.servers': 'localhost:9092',  
    }
    topic = 'my_topic'
    
    produce_messages(producer_config, topic)
