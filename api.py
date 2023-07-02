from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def serve():
    with open('response.json') as user_file:
        jsonStr = json.load(user_file)

    return jsonStr

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)