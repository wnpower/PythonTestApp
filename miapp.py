from flask import Flask
import os

MyApp = Flask(__name__)

@MyApp.route("/")
def hello():
    return "This is Hello World!\n"

if __name__ == "__main__":
    MyApp.run(host='0.0.0.0', port=12345)
