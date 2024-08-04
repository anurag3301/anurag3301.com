from flask import Flask, jsonify, send_from_directory, abort
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__,  static_url_path='')
CORS(app)

@app.route('/')
@cross_origin()
def index():
    return "hello"

@app.route('/blog/', defaults={'path': 'index.html'})
@app.route('/blog/<path:path>')
def serve_blog_static(path):
    file_path = os.path.join('blog/public', path)
    if os.path.isfile(file_path):
        return send_from_directory('blog/public', path)
    elif os.path.isdir(file_path):
        return send_from_directory(file_path, 'index.html')
    else:
        return abort(404)

if __name__ == "__main__":
    app.run(debug=True)
