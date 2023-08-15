from flask import Flask, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    # take inputs from body
    body = request.get_json()
    sum=body['first']+body['second']
    #return json response
    return {"result":sum}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    body = request.get_json()
    diff=body['first']-body['second']
    #return json response
    return {"result":diff}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
