from flask import Flask
import os
import sys

MyApp = Flask(__name__)

@MyApp.route("/")
def hello():
    return "This is Hello World!. Python version: " + sys.version + "\n"

if __name__ == "__main__":
    MyApp.run(host='0.0.0.0', port=12345)
