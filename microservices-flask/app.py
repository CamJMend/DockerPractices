from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suma', methods=['GET'])
def suma():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({'resultado': a + b})

@app.route('/resta', methods=['GET'])
def resta():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({'resultado': a - b})

@app.route('/multiplicacion', methods=['GET'])
def multiplicacion():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({'resultado': a * b})

@app.route('/division', methods=['GET'])
def division():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    if b == 0:
        return jsonify({'error': 'División por cero no permitida'}), 400
    return jsonify({'resultado': a / b})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)