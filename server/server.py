import os
import sys
import grpc
from concurrent import futures

# Ensure 'stubs/' is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "stubs")))

# Import generated gRPC code
import helloworld_pb2 as helloworld_pb2 #type: ignore
import helloworld_pb2_grpc as helloworld_pb2_grpc #type: ignore

class GreeterServicer(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("✅ Server started on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
