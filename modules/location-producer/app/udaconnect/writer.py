import grpc
import location_pb2
import location_pb2_grpc

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:30002")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    person_id=1,
    latitude=1.234,
    longitude=5.678
)

response = stub.Create(location)
print(response)
