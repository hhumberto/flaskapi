from flask import Flask, render_template
# from flask_parameter_validation import ValidateParameters, Route, Json, Query
# from datetime import datetime

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


@app.route("/")
def hello():
    return "<h2>Para empezar</h2>"


# @app.route("/<string:name>/")
# def say_hello(name):
#     return f"What's so matter {name}!"
@app.route("/login")
@app.route("/login/<variable>")
# @ValidateParameters()
def login(variable=None):
    return render_template("index.html", name=variable)

if __name__ == "__main__":
    app.run()
