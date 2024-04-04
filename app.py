from fastapi import FastAPI
from typing import Dict, Any
import yaml

app = FastAPI()

@app.get("/api/resources")
def get_resources() -> Dict[str, Any]:
    try:
        with open('data/ebbcarbon.yaml', 'r') as file:
            resources = yaml.safe_load(file)
        return {"statusCode": 200, "body": resources}
    except FileNotFoundError:
        return {"statusCode": 404, "body": "Resource file not found"}
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}