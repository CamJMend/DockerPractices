from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Microservicios de Cálculo de Áreas</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    line-height: 1.6;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                h2 {
                    color: #555;
                    margin-top: 30px;
                }
                .endpoint {
                    background-color: #f5f5f5;
                    padding: 15px;
                    border-radius: 5px;
                    margin-bottom: 20px;
                }
                .url {
                    font-family: monospace;
                    background-color: #e9e9e9;
                    padding: 5px;
                    border-radius: 3px;
                }
            </style>
        </head>
        <body>
            <h1>Microservicios para Cálculo de Áreas</h1>
            <p>Esta aplicación proporciona tres microservicios para calcular áreas de figuras geométricas:</p>
            
            <div class="endpoint">
                <h2>Área de un Triángulo</h2>
                <p>Calcula el área de un triángulo usando base y altura.</p>
                <p>Endpoint: <span class="url">/area/triangulo?base=5&altura=3</span></p>
            </div>
            
            <div class="endpoint">
                <h2>Área de un Cuadrado</h2>
                <p>Calcula el área de un cuadrado usando la longitud del lado.</p>
                <p>Endpoint: <span class="url">/area/cuadrado?lado=4</span></p>
            </div>
            
            <div class="endpoint">
                <h2>Área de un Círculo</h2>
                <p>Calcula el área de un círculo usando el radio.</p>
                <p>Endpoint: <span class="url">/area/circulo?radio=5</span></p>
            </div>
        </body>
    </html>
    '''

@app.route('/area/triangulo', methods=['GET'])
def area_triangulo():
    try:
        base = float(request.args.get('base'))
        altura = float(request.args.get('altura'))
        
        if base <= 0 or altura <= 0:
            return jsonify({'error': 'La base y la altura deben ser valores positivos'}), 400
            
        area = (base * altura) / 2
        return jsonify({
            'figura': 'triángulo',
            'base': base,
            'altura': altura,
            'area': area
        })
    except (ValueError, TypeError):
        return jsonify({'error': 'Parámetros inválidos. Se requieren valores numéricos para base y altura'}), 400

@app.route('/area/cuadrado', methods=['GET'])
def area_cuadrado():
    try:
        lado = float(request.args.get('lado'))
        
        if lado <= 0:
            return jsonify({'error': 'El lado debe ser un valor positivo'}), 400
            
        area = lado * lado
        return jsonify({
            'figura': 'cuadrado',
            'lado': lado,
            'area': area
        })
    except (ValueError, TypeError):
        return jsonify({'error': 'Parámetro inválido. Se requiere un valor numérico para el lado'}), 400

@app.route('/area/circulo', methods=['GET'])
def area_circulo():
    try:
        radio = float(request.args.get('radio'))
        
        if radio <= 0:
            return jsonify({'error': 'El radio debe ser un valor positivo'}), 400
            
        area = math.pi * radio * radio
        return jsonify({
            'figura': 'círculo',
            'radio': radio,
            'area': area
        })
    except (ValueError, TypeError):
        return jsonify({'error': 'Parámetro inválido. Se requiere un valor numérico para el radio'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)