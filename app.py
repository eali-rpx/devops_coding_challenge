from flask import Flask, jsonify
import yaml

app = Flask(__name__)

@app.route('/api/resources', methods=['GET'])
def get_resources():
    try:
        with open('data/ebbcarbon.yaml', 'r') as file:
            resources = yaml.safe_load(file)
        return jsonify({'resources': resources})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)