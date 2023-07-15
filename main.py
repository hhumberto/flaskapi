
from flask import Flask, render_template, abort, redirect, sessions, url_for
# from flask_parameter_validation import ValidateParameters, Route, Json, Query
# from datetime import datetime

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


@app.route("/")
def hello():
    return "<h2>Para empezar CON GITHUB</h2>"


@app.route('/logeo')
def test():   
    name = "Este si es valor"
    return render_template("index.html", name=name)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    
    return 'This is other thing'

if __name__ == "__main__":
    app.run()
