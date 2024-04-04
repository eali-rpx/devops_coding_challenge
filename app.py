from flask import (Flask, jsonify)
import yaml
from flask_lambda import FlaskLambda

app = FlaskLambda(__name__)

@app.route('/api/resources', methods=['GET'])
def get_resources():
    try:
        with open('data/ebbcarbon.yaml', 'r') as file:
            resources = yaml.safe_load(file)
        return jsonify(resources), 200
    except FileNotFoundError:
        return "Resource file not found", 404
    except Exception as e:
        return str(e), 500