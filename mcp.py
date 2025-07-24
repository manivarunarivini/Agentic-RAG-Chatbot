class MCPMessage:
    def __init__(self, sender, receiver, payload, trace_id):
        self.sender = sender
        self.receiver = receiver
        self.trace_id = trace_id
        self.payload = payload

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "trace_id": self.trace_id,
            "payload": self.payload
        }
