##__author__ = 'rites'

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"


@app.route("/user/<username>/")
def hello_user(username):
    return str("Hello Mr. "+ username + "!!!")


if __name__ == "__main__":
    app.run()
