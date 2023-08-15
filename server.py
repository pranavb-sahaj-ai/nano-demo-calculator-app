from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    print("Yokoso")

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Helo World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    numbers = request.json
    result = numbers['first'] + numbers['second']
    return {'result': result}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    numbers = request.json
    result = numbers['first'] - numbers['second']
    return {'result': result}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
