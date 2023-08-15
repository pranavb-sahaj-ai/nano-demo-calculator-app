from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    res=request.get_json()
    return {"result":res['first']+res['second']}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    res=request.get_json()
    return {"result":res['first']-res['second']}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
