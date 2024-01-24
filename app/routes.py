from flask import Blueprint, jsonify
from functions.stockRl import get_results

bp = Blueprint('routes', __name__)

@bp.route('/get_results', methods=['GET'])
def send():
     results = get_results()

    # Convert DataFrame to a dictionary
     results_dict = results.to_dict(orient='records')

    # Return the dictionary as JSON
     return jsonify(results_dict)