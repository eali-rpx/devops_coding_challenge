from flask import Flask, jsonify
import yaml
from yaml.loader import SafeLoader
from mangum import Mangum

app = Flask(__name__)

@app.route('/api/resources', methods=['GET'])
def app(filename):
    with open(f'data/{filename}.yaml','r') as f:
        output = yaml.safe_load(f)
    
    # Check if 'resources' key exists in the YAML data
    if 'resources' in output:
        print(output['resources'])
    else:
        print("'resources' key not found in the YAML file.")

handler = Mangum(app=app)