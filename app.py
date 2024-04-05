import awsgi
from flask import Flask

app = Flask(__name__)

@app.route('/api/resources', methods=['GET'])
def get_resources():
    return "Hi EBBCARBOON", 200

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})