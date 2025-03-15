import argparse
import subprocess
import utils.generate_protos
import os

PROTO_FILE = "proto/helloworld.proto"
STUB_FILE = "stubs/helloworld_pb2.py"

def needs_regeneration():
    """Check if the .proto file is newer than the generated stubs."""
    if not os.path.exists(STUB_FILE):
        return True  # No stubs exist yet, generate them

    proto_time = os.path.getmtime(PROTO_FILE)
    stub_time = os.path.getmtime(STUB_FILE)
    return proto_time > stub_time  # Regenerate only if .proto is newer

def generate_stubs():
    """Regenerate gRPC stubs only if necessary."""
    if needs_regeneration():
        print("🔄 Regenerating gRPC stubs...")
        utils.generate_protos.generate_protos()
    else:
        print("✅ Stubs are up-to-date. No regeneration needed.")

def start_server():
    print("🚀 Starting gRPC Server...")
    subprocess.run(["python", "server/server.py"])

def start_client():
    print("📡 Starting gRPC Client...")
    subprocess.run(["python", "client/client.py"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run gRPC server or client")
    parser.add_argument("mode", choices=["server", "client"], help="Start gRPC server or client")
    args = parser.parse_args()

    generate_stubs()  # Only regenerate if needed

    if args.mode == "server":
        start_server()
    elif args.mode == "client":
        start_client()