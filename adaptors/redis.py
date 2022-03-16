class MockedRedis:
    def __init__(self):
        self.redis_uri = 'localhost:6379'

    @staticmethod
    def get_discount_code(code):
        return {}

    # will put discount code, and it's usage maximum count in redis
    @staticmethod
    def put_discount_code(discount):
        return

    @staticmethod
    def use_one(code):
        # will edit the key in redis and will subtract from its current usage ("code", 17) ==> ("code", 16)
        return {}
