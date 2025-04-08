# api_server.py

from flask import Flask, request, jsonify
from node_store import NodeStore

app = Flask(__name__)
store = NodeStore()

@app.route('/')
def home():
    return "Distributed Cluster Simulation API Running"

@app.route('/register_node', methods=['POST'])
def register_node():
    data = request.get_json()
    node_id = data.get("node_id")
    cpu_cores = data.get("cpu_cores")

    if not node_id or cpu_cores is None:
        return jsonify({"error": "Missing node_id or cpu_cores"}), 400

    success = store.register_node(node_id, cpu_cores)
    if success:
        return jsonify({"message": f"Node '{node_id}' registered with {cpu_cores} cores."}), 200
    else:
        return jsonify({"message": f"Node '{node_id}' already exists."}), 409

@app.route('/list_nodes', methods=['GET'])
def list_nodes():
    return jsonify(store.get_all_nodes())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
