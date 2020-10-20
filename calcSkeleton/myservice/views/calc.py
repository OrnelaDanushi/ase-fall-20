from flakon import JsonBlueprint
# from flask import Flask,
from flask import request, jsonify
from myservice.calculator import calculator as c


calc = JsonBlueprint('calc', __name__)


@calc.route('/calc/sum', methods=['GET'])
def sum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.sum(m, n)

    return jsonify({'result': str(result)})


# from here implement also the other operations
@calc.route('/calc/div', methods=['GET'])
def div():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.divide(m, n)

    try:
        return jsonify({'result': str(result)})
    except ZeroDivisionError:
        return jsonify({'result': 'You cannot divide by 0!'})


@calc.route('/calc/multiply', methods=['GET'])
def multiply():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.multiply(m, n)

    return jsonify({'result': str(result)})


@calc.route('/calc/subtract', methods=['GET'])
def subtract():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.subtract(m, n)

    return jsonify({'result': str(result)})
