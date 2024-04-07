from fastapi import FastAPI
from mangum import Mangum
import yaml
import logging

# API Application object
app = FastAPI()

file_path = 'data/ebbcarbon.yaml'

@app.get('/resources')
def get_resources():
    with open(file_path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)

    return data['resources']

handler = Mangum(app=app)

# Self contained application
if __name__ == "__main__":
    # Run with uvicorn: uvicorn main:app --reload
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8080, log_level="info", reload=True)
