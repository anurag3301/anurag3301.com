from flask import Flask, jsonify, send_from_directory
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__, static_folder='client/build', static_url_path='')
CORS(app)

@app.route('/api/data')
@cross_origin()
def get_data():
    data = {'message': 'Testing Github Action CICD'}
    return jsonify(data)


@app.route('/api/attendance')
@cross_origin()
def attendance_data():
    data = {'dscc': 61.90,
            'ml': 63.16,
            'mad': 71.43,
            'arvr': 54.55,
            'vap': 70,
            'pw': 92.31,
            }
    return jsonify(data)

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)
