from datetime import datetime
from flask import Blueprint, request, jsonify
from .views import RegressionModel
from .models import get_all_data

regression_bp = Blueprint('regression', __name__)

regression_model = RegressionModel()

# Entrena la data cada vez que se inicia la aplicación
@regression_bp.before_request
def train_titanic_model():
    regression_model.train()


# Método de ayuda para determinar si la aplicación responde correctamente
@regression_bp.route('/ping')
def endpoint2():
    return jsonify(message="pong")


# Devuelve todo el dataset guardado en la base de datos
@regression_bp.route('/data', methods=['GET'])
def get_all_data():
    data = get_all_data()
    return jsonify(data)

# Método donde se hace la predicción de acuerdo a los parametros del Body
@regression_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = regression_model.predict(data)
    prediction = int(prediction)
    if prediction == 1:
        return jsonify(prediction="El pasajero sobrevive", value=prediction, prediction_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        return jsonify(prediction="El pasajero no sobrevive", value=prediction, prediction_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
