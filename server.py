from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.')
CORS(app)

def clasificar_recuperacion(valor):
    if valor < 50.0:
        return {
            "texto": "BAJA (Requiere Optimizacion)",
            "color": "#ff6b6b",
            "semaforo": "rojo"
        }
    elif 50.0 <= valor <= 75.0:
        return {
            "texto": "MEDIA (Rango Estandar)",
            "color": "#feca57",
            "semaforo": "amarillo"
        }
    else:
        return {
            "texto": "ALTA (Eficiencia Optima)",
            "color": "#1dd1a1",
            "semaforo": "verde"
        }

@app.route('/')
def index():
    return send_from_directory('.', 'ai_studio_code.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

@app.route('/api/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    try:
        metal = data.get('metal', 'au')
        x1 = float(data.get('x1', 8))
        x2 = float(data.get('x2', 10))
        x3 = float(data.get('x3', 5))
        x4 = float(data.get('x4', 150))
        x5 = float(data.get('x5', 12))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid parameter values"}), 400
    
    if metal not in ('au', 'ag'):
        return jsonify({"error": "Metal must be 'au' or 'ag'"}), 400
    
    if not (0 <= x1 <= 14):
        return jsonify({"error": "pH (x1) must be between 0 and 14"}), 400
    if not (0 <= x2 <= 100):
        return jsonify({"error": "Sulfides (x2) must be between 0 and 100"}), 400
    if x3 < 0:
        return jsonify({"error": "Grade (x3) must be non-negative"}), 400
    if x4 < 0:
        return jsonify({"error": "Collector (x4) must be non-negative"}), 400
    if x5 < 0:
        return jsonify({"error": "Grinding time (x5) must be non-negative"}), 400
    
    if metal == 'au':
        c_base = 35.5
        c_ph = -4.2 * x1
        c_sulf = 0.35 * x2
        c_ley = 1.8 * x3
        c_col = 0.15 * x4
        c_mol = 0.8 * x5
    else:
        c_base = 30.0
        c_ph = -3.8 * x1
        c_sulf = 0.40 * x2
        c_ley = 0.05 * x3
        c_col = 0.12 * x4
        c_mol = 0.9 * x5
    
    recuperacion = c_base + c_ph + c_sulf + c_ley + c_col + c_mol
    recuperacion = max(0.0, min(100.0, recuperacion))
    
    components = [c_base, c_ph, c_sulf, c_ley, c_col, c_mol]
    clasificacion = clasificar_recuperacion(recuperacion)
    
    return jsonify({
        "recuperacion": recuperacion,
        "clasificacion": clasificacion,
        "components": components
    })

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
