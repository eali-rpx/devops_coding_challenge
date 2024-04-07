from flask import Flask, jsonify
import yaml

app = Flask(__name__)

@app.route('/api/resources', methods=['GET'])
def get_resources():
    try:
        with open('data/ebbcarbon.yaml', 'r') as f:
            data = yaml.safe_load(f)
            resources = data.get('resources', [])
            return jsonify(resources)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)