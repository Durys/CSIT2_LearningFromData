from flask import Flask

from Backend.csv_to_json import csv_to_json

app = Flask(__name__)


@app.route('/data', methods=['GET', 'POST'])
def start():
    csv_to_json()


# Run
if __name__ == '__main__':
    app.run()

