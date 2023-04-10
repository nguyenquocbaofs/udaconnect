import json
from kafka import KafkaConsumer
from services import LocationService

TOPIC_NAME = 'location'
KAFKA_SERVER = ['kafka-service:9092']
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)


for message in consumer:
    print("Received a message: ", message)
    location = json.loads(message.value)
    LocationService.create(location)
    print("Location added to database successfully")
