from flask import Blueprint, jsonify

knn_bp = Blueprint('knn', __name__)

@knn_bp.route('/ping')
def endpoint2():
    return jsonify(message="pong")