from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h2>Para empezar</h2>"


@app.route("/<string:name>/")
def say_hello(name):
    return f"What's so matter {name}!"


if __name__ == "__main__":
    app.run()
