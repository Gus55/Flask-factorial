from flask import Flask, jsonify, request
from math import factorial

app = Flask(__name__)

lfact = []

@app.route('/<number>')
def home(number):
  number=int(number)
  factorial_total = 1
  while number > 1:
      factorial_total *= number
      number -= 1

  lfact = []
  facto = {
      "Factorial": factorial_total ,
  }
  lfact.append(facto)
  return jsonify(lfact)

@app.route('/<number>', methods=['POST'])
def add_fact(number):
    number=int(number)
    factorial_total = 1
    while number > 1:
        factorial_total *= number
        number -= 1

    lfact = []
    facto = {
        "Factorial": factorial_total ,
    }
    lfact.append(facto)
    return jsonify(lfact)
    #return jsonify(number)

if __name__ == '__main__':
  app.run(debug=True)
