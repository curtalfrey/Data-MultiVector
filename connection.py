# connection.py

class Connection:
    def __init__(self, source, destinations, allowed_modifications):
        self.source = source
        self.destinations = destinations
        self.allowed_modifications = allowed_modifications

    def process_data(self, data):
        # Process data according to connection rules
        processed_data = data  # Placeholder, implement actual processing logic
        return processed_data

def create_connections(connection_data):
    connections = []
    for source, destinations, allowed_modifications in connection_data:
        connection = Connection(source, destinations, allowed_modifications)
        connections.append(connection)
    return connections
