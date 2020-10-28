import flask
from flask import Flask
import json


from Backend.csv_to_json import csv_to_json

app = Flask(__name__)


@app.route('/from_csv', methods=['GET'])
def start():
    data = csv_to_json()
    return json.dumps(data, indent=4)


@app.route("/movies", methods=["POST"])
def get_data():
    json_data = flask.request.json
    return "JSON value sent: " + json_data


# Run
if __name__ == '__main__':
    app.run()
