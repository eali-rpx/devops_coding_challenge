from flask import Flask, jsonify
from urllib.parse import quote as url_quote
import yaml

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')