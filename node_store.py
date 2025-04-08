# node_store.py

class NodeStore:
    def __init__(self):
        self.nodes = {}

    def register_node(self, node_id, cpu_cores):
        if node_id in self.nodes:
            return False  # already exists
        self.nodes[node_id] = {
            "cpu_cores": cpu_cores,
            "available_cpu": cpu_cores,
            "pods": [],
            "status": "healthy"
        }
        return True

    def get_all_nodes(self):
        return self.nodes
