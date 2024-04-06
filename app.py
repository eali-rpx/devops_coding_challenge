import yaml
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Union

app = FastAPI()
handler = Mangum(app)

def get_yaml_data(filename):
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    return data

@app.get('/api/resources')
def get_resources():
    # Get the data from the YAML file
    data = get_yaml_data("data/ebbcarbon.yaml")
    
    # Extract the "resources" part
    resources = data.get("resources")
    
    # Return response
    return JSONResponse(content=resources)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
