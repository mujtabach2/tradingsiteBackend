from app import app
from flask import Blueprint, jsonify
from functions.stockRl import get_results
bp = Blueprint('routes', __name__)

@bp.route('/get_results', methods=['GET'])
def send():
    results = get_results()
    return jsonify(results)
