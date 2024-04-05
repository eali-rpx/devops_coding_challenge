from flask import Flask

app = Flask(__name__)

@app.route('/api/resources', methods=['GET'])
def get_resources():
    return "Hi EBBCARBOON", 200

if __name__ == '__main__':
    app.run(debug=True)