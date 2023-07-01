from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def serve():
    jsonStr = "{'Test':1234}"

    return jsonStr

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)