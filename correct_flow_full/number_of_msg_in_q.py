from pulsar import Client

pulsar_url = 'pulsar://localhost:6650'
topic_name = 'persistent://public/default/my-topic'
subscription_name = 'test-subscription'

client = Client(pulsar_url)
consumer = client.subscribe(topic_name, subscription_name)

try:
    # Try to receive a single message
    msg = consumer.receive(timeout_millis=5000)  # Adjust the timeout as needed
    print(f"Received message: {msg.data()}")
    consumer.acknowledge(msg)
except Exception as e:
    print("No message received or error:", e)

client.close()
