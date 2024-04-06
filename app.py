from flask import Flask
import yaml


def app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route("/api/resources")
    def get_resources():
        with open("data/ebbcarbon.yaml", "r", encoding="UTF-8") as endpoint_data:
            try:
                company_data = yaml.safe_load(endpoint_data)
            except yaml.YAMLError:
                return "Server Error", 500

        return company_data["resources"]

    return app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)