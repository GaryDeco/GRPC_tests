import os
import sys
import grpc

# Ensure 'stubs/' is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "stubs")))

# Import generated gRPC code
import helloworld_pb2 as helloworld_pb2 #type: ignore
import helloworld_pb2_grpc as helloworld_pb2_grpc #type: ignore

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="World"))
        print(f"✅ Greeter response: {response.message}")

if __name__ == "__main__":
    run()