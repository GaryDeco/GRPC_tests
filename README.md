### 🚀 **gRPC Python Project**
This project demonstrates a **basic gRPC setup** in Python, with a **structured folder layout** for managing `.proto` files, generated stubs, server, and client implementations.

---

## 📂 **Project Structure**
```
GRPC_tests/
│── main.py                 # Entry point to start server or client
│── proto/                   # Stores .proto files
│   ├── helloworld.proto
│── stubs/                   # Stores generated gRPC Python code
│   ├── __init__.py          # Marks as a package
│   ├── helloworld_pb2.py
│   └── helloworld_pb2_grpc.py
│── server/                  # Server implementation
│   ├── server.py
│   └── __init__.py
│── client/                  # Client implementation
│   ├── client.py
│   └── __init__.py
│── utils/                   # Stores utility scripts
│   ├── generate_protos.py   # Generates gRPC stubs
│   └── __init__.py
│── venv/                    # Virtual environment (if used)
└── requirements.txt          # Dependencies list
```

---

## 🔧 **Setup & Installation**
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-repo-name.git
cd GRPC_tests
```

### 2️⃣ **Create a Virtual Environment (Optional, Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Generate gRPC Stubs**
Run this command to compile `.proto` files:
```bash
python utils/generate_protos.py
```

---

## 🚀 **Usage**
### ✅ **Start the Server**
```bash
python main.py server
```

### ✅ **Run the Client**
```bash
python main.py client
```

---

## 🔧 **Modify `.proto` Files**
1. **Edit `proto/helloworld.proto`**
2. **Regenerate gRPC code:**
   ```bash
   python utils/generate_protos.py
   ```
3. **Restart the server & client**

---

## 🛠 **Troubleshooting**
### ❓ **ImportError: No module named 'stubs'**
✔ Solution: Ensure `stubs/` is recognized as a package:
```bash
touch stubs/__init__.py  # Linux/Mac
echo > stubs/__init__.py  # Windows
```
✔ Alternatively, modify `settings.json` in VS Code:
```json
{
    "python.analysis.extraPaths": [
        "./stubs"
    ]
}
```

---

## 🛠 **Contributing**
Feel free to submit issues and pull requests! Contributions are welcome. 🚀

---

## 📜 **License**
This project is licensed under the **MIT License**.

---

### 🎯 **Next Steps**
- 🔒 Add **TLS encryption** for secure gRPC communication
- 🔄 Implement **bidirectional streaming**
- 🐳 Dockerize the server & client for easy deployment

