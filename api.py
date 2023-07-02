from flask import Flask,jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def serve():
    with open('response.json') as user_file:
        jsonStr = json.load(user_file)
    response = jsonify(jsonStr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)