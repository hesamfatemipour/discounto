from flask import Flask

app = Flask(__name__)


@app.route("/discount", methods=['GET'])
def get_discount_code(code):
    pass


@app.route("/discount", methods=['POST'])
def create_discount_code():
    pass


@app.route("/discount", methods=['DELETE'])
def create_discount_code():
    pass
