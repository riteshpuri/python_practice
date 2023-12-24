__author__ = 'rites'

from flask import Flask, render_template
import random
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World"


@app.route("/")
def hello():
  return "Hello World!!! I've run my first Flask application."

@app.route("/user/<username>/")
def hello_user1(username):
    return str("Hello Mr. "+ username + "!!!")


quotes = [
               "Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
               "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
               "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
               "Listen to many, speak to a few.",
               "Only when the tide goes out do you discover who has been swimming naked."
   ]
@app.route("/hello/<username>/")
def hello_user(username):
  return """<h2>Hello {}</h2></br>
         <h3>Quote of the Day for You</h3>
         {}
         """.format(username, random.choice(quotes))

@app.route("/quotes/")
def display_quotes():
    print('display_quotes')
    return render_template("myquotes.html", data=quotes)


if __name__ == "__main__":
    app.run()
