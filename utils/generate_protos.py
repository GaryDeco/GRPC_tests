import os
import subprocess

PROTO_DIR = os.path.join(os.path.dirname(__file__), "..", "proto")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "stubs")

def generate_protos():
    """Run protoc to generate gRPC Python code."""
    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)
    
    command = f"python -m grpc_tools.protoc -I {PROTO_DIR} --python_out={OUT_DIR} --grpc_python_out={OUT_DIR} {PROTO_DIR}/helloworld.proto"
    subprocess.run(command, shell=True, check=True)
    print("✅ gRPC Python code generated successfully in 'stubs/'.")

if __name__ == "__main__":
    generate_protos()