from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from functions.stockRl import get_results

bp = Blueprint('routes', __name__)

# Enable CORS for all routes on the blueprint
CORS(bp)

@bp.route('/get_results', methods=['GET'])
def send():
    results = get_results()

    # Convert DataFrame to a dictionary
    results_dict = results.to_dict(orient='records')

    # Return the dictionary as JSON
    return jsonify(results_dict)
