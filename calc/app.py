# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addR():
    """Add a to b"""
    a = int(request.args.get['a'])
    b = int(request.args.get['b'])
    return str(add(a,b))

@app.route('/sub')
def subR():
    """Subtract a by b"""
    a = int(request.args.get['a'])
    b = int(request.args.get['b'])
    return str(sub(a,b))

@app.route('/mult')
def multR():
    """Multiply a by b"""
    a = int(request.args.get['a'])
    b = int(request.args.get['b'])
    return str(mult(a,b))

@app.route('/div')
def divR():
    """Divide a by b"""
    a = int(request.args.get['a'])
    b = int(request.args.get['b'])
    return str(div(a,b))


operations = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<operation>")
def math(operation):
    """Do operation on a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations[operation](a, b))
