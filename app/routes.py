from app import app
from flask import jsonify, request

from functions.stockRl import get_results
@app.route('/get_results', methods=['GET'])
def send():
    results = get_results()
    return jsonify(results)
