import os
import subprocess
import sys

'''
Run this script to set up a virtual environment and install gRPC and gRPC tools.
'''

def run_command(command, check=True):
    """Run a shell command and print the output"""
    try:
        subprocess.run(command, shell=True, check=check)
        print(f"✔ Successfully ran: {command}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to run: {command}")
        sys.exit(1)

def setup_virtualenv():
    """Set up and activate a virtual environment"""
    if not os.path.exists("venv"):
        print("📂 Creating virtual environment...")
        run_command(f"{sys.executable} -m pip install --upgrade pip")
        run_command(f"{sys.executable} -m pip install virtualenv")
        run_command(f"{sys.executable} -m virtualenv venv")

    print("✅ Virtual environment set up.")
    activate_script = "venv\\Scripts\\activate" if os.name == "nt" else "source venv/bin/activate"
    print(f"🔧 Run `{activate_script}` to activate the virtual environment.")

def install_grpc():
    """Install gRPC and related tools"""
    print("📦 Installing gRPC and gRPC tools...")
    run_command("venv\\Scripts\\python -m pip install --upgrade pip" if os.name == "nt" else "source venv/bin/activate && python -m pip install --upgrade pip")
    run_command("venv\\Scripts\\python -m pip install grpcio grpcio-tools" if os.name == "nt" else "source venv/bin/activate && python -m pip install grpcio grpcio-tools")
    print("✅ gRPC installation complete.")

if __name__ == "__main__":
    setup_virtualenv()
    install_grpc()
    print("\n🚀 Setup complete! If needed, activate your virtual environment using `venv\\Scripts\\activate` and start working on gRPC.")