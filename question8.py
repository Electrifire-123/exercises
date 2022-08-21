from flask import Flask,jsonify
import math

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello world</h1>"

@app.route("/fibonacci/<string:num>")
def fibonacci(num):
    number = int(num)

    def prfctsqr(x):
        s = int(math.sqrt(x))
        return s*s == x
    
    firstchck = 5*(number*number)+4
    secondchck = 5*(number*number)-4
    
    if prfctsqr(firstchck) or prfctsqr(secondchck):
        data1={
            "username":"Rahul Yadav",
            "serverid" : "123.145.12.6",
            "number" : number,
            "fibonacci": True

        }
        return jsonify(data1)
    else:
        data1 = {
            "username":"Akash Vaidya",
            "serverid" : "123.145.12.6",
            "number" : number,
            "fibonacci": False
        }
        return jsonify(data1)


if __name__ =="__main__":
    app.run(debug=True)
