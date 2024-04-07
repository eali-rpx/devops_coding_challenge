from flask import Flask, jsonify
import yaml
from yaml.loader import SafeLoader

app = Flask(__name__)

@app.route('/api/resources/<filename>', methods=['GET'])
def get_resources(filename):
    try:
        with open(f'data/{filename}.yaml', 'r') as f:
            output = yaml.safe_load(f)
        
        # Check if 'resources' key exists in the YAML data
        if 'resources' in output:
            return jsonify(output['resources'])
        else:
            return jsonify({"error": "'resources' key not found in the YAML file."}), 404
    except FileNotFoundError:
        return jsonify({"error": "File not found."}), 404

# Lambda handler
def lambda_handler(event, context):
    # Use the event to get the filename parameter from the URL
    filename = event['pathParameters']['filename']
    
    # Call the Flask app with the filename parameter
    response = app.dispatch_request('GET', f'/api/resources/{filename}')
    
    # Return the Flask app response
    return {
        'statusCode': response.status_code,
        'body': response.get_data(as_text=True),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
