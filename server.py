from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    print("Yokoso")

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return ''

@app.route("/calculator/add", methods=['POST'])
def add():
    first = request.args.get('first')
    second = request.args.get('second')
    return {'result': int(first) + int(second)}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    first = request.args.get('first')
    second = request.args.get('second')
    return {'result': int(first) - int(second)}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
