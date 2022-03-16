class MockedNats:
    def __init__(self):
        self.nats_uri = "localhost"
        self.nats_topic = "discount_consume"

    # will publish an event on a discount being consumed
    @staticmethod
    async def publish(payload):
        return {}
