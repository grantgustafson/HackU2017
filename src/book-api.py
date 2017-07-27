import os, sys
from flask import Flask
from config import LOGGER
from api.query import query

app = Flask(__name__)

app.register_blueprint(query)
if __name__ == '__main__':
    app.run(host="0.0.0.0")
