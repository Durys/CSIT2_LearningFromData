import flask
from flask import Flask


from Backend.csv_to_json import csv_to_json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def start():
    csv_to_json()


@app.route("/", methods=["GET"])
def get_data():
    json_data = flask.request.json
    return "JSON value sent: " + json_data


# Run
if __name__ == '__main__':
    app.run()

