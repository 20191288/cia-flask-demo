from flask import Blueprint, jsonify

regression_bp = Blueprint('regression', __name__)

@regression_bp.route('/ping')
def endpoint2():
    return jsonify(message="pong")