from datetime import datetime
from flask import Flask

app = Flask(__name__)
count = 0

@app.route("/")
def welcome():
    return "Welcome to the flash cards application!!!"


@app.route("/viewcount")
def viewcount():
    global count
    count += 1
    return "Page was viewed " + str(count) + " times."


@app.route("/date")
def date():
    return "This page was serverd at " + str(datetime.now())
