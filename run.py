from flask import Flask
from adaptors.db import MockedDB
from adaptors.redis import MockedRedis

app = Flask(__name__)


@app.route("/discount", methods=['GET'])
def get_discount_code(code):
    discount = MockedRedis.get_discount_code(code)
    return discount if discount else MockedDB.retrieve(code)


@app.route("/discount", methods=['POST'])
def create_discount_code(payload):
    discount = MockedDB.insert(payload)
    MockedRedis.put_discount_code(discount)
    return 204


@app.route("/discount", methods=['PATCH'])
def consume_discount_code(code):
    MockedRedis.use_one(code)
    MockedDB.consume(code, -1)
    return
