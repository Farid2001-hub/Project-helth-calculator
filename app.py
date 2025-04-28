from flask import Flask, render_template, request, jsonify
from utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi_endpoint():
    try:
        # Récupération des données envoyées en JSON
        data = request.get_json()
        height = float(data['height'])
        weight = float(data['weight'])

        # Calcul du BMI
        bmi = calculate_bmi(height, weight)

        # Retourner les résultats sous forme de JSON
        return jsonify({
            'bmi': bmi
        })
    except (ValueError, KeyError):
        return jsonify({
            'error': 'Invalid input. Please provide valid numeric values for height and weight.'
        }), 400

@app.route('/calculate_bmr', methods=['POST'])
def calculate_bmr_endpoint():
    try:
        # Récupération des données envoyées en JSON
        data = request.get_json()
        height = float(data['height'])
        weight = float(data['weight'])
        age = int(data['age'])
        gender = data['gender'].lower()

        # Calcul du BMR
        bmr = calculate_bmr(height, weight, age, gender)

        # Retourner les résultats sous forme de JSON
        return jsonify({
            'bmr': bmr
        })
    except (ValueError, KeyError):
        return jsonify({
            'error': 'Invalid input. Please provide valid numeric values for height, weight, age, and a valid gender (male/female).'
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
