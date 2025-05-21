from flask import Flask, render_template, request, jsonify
import tsp
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', cities=tsp.CITIES.keys())

@app.route('/solve', methods=['POST'])
def solve():
    data = request.form
    normal_temp = float(data['normal_temp'])
    min_temp = float(data['min_temp'])
    cooling_rate = int(data['cooling_rate'])
    origin_city = data['origin_city']
    destination_city = data['destination_city']

    ruta = list(tsp.CITIES.keys())
    random.shuffle(ruta)

    ruta_optima = tsp.simulated_annealing(ruta, tsp.CITIES, normal_temp, min_temp, cooling_rate)
    distancia_total = tsp.evalua_ruta(ruta_optima, tsp.CITIES)

    return jsonify({'ruta': ruta_optima, 'distancia_total': distancia_total})

if __name__ == '__main__':
    app.run(debug=True)
