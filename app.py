import yaml
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_yaml_data(filename):
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    return data

@app.route('/api/resources', methods=['GET'])
def get_resources():
    # Get the data from the YAML file
    data = get_yaml_data("data/ebbcarbon.yaml")
    
    # Extract the "resources" part
    resources = data.get("resources")
    
    # Return response
    return jsonify(resources), 200

if __name__ == '__main__':
    app.run(debug=True)
