from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def serve():
    with open('response.json') as user_file:
        jsonStr = json.load(user_file)

    return jsonStr

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)