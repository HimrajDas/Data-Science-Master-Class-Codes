from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/")
def hello_word():
    return "Hello, World!"


@app.route("/hello1")
def hello_word1():
    return "Hello, World1!"


@app.route("/hello2")
def hello_word2():
    return "Hello, World2!"

@app.route("/input")
def request_input():
    data = request.args.get("x")
    return f"This is my return from url {data}"






if __name__ == "__main__":
    app.run(host="0.0.0.0")
