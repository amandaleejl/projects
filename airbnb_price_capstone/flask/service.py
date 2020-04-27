from flask import Flask, jsonify, request
from sklearn.linear_model import LogisticRegression
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World’


if __name__ == '__main__':
    app.run()
