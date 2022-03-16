class MockedDB:
    def __init__(self):
        self.db_uri = ''
        self.db_name = 'main'
        self.table_name = 'discounts'

    @classmethod
    def insert(cls, payload):
        return {}

    @classmethod
    def retrieve(cls, code):
        return {}

    @classmethod
    def delete(cls):
        return

    @classmethod
    def update(cls, code, payload):
        return

    @classmethod
    def consume(cls, code, update_payload):
        discount = cls.retrieve(code)
        cls.update(discount, update_payload)
        return discount
