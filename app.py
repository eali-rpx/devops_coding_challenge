import serverless_wsgi
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_resources():
    return "Hi EBBCARBOON", 200

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)

if __name__ == '__main__':
    app.run(debug=True)