from flask import Flask
import os

application = Flask(__name__)

@application.route("/")
def hello():
    return "This is Hello World!\n"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=12345)
