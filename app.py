from flask import Flask, jsonify

from deposit_funds import deposit_funds

app = Flask(__name__)

@app.route("/", methods = ['GET'] )
def func():
    return jsonify({"message": "Hello World"})

@app.route("/deposit", methods = ['GET'])
def deposit_function():
    resp = deposit_funds()
    return jsonify(resp)

if __name__ == '__main__':
    app.run(debug=True)