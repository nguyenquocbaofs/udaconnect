import time
from concurrent import futures

from kafka import KafkaProducer

import grpc
import location_pb2
import location_pb2_grpc


TOPIC_NAME = 'location'
KAFKA_SERVER = 'kafka-service:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                         api_version=(0, 11, 5))


class LocationService(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        location = {
            "person_id": request.person_id,
            "latitude": request.latitude,
            "longitude": request.longitude
        }
        producer.send(TOPIC_NAME, location)
        producer.flush()
        return location_pb2.LocationMessage(**location)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(
    LocationService(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
