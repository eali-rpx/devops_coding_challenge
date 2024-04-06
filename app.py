from typing import Union
from fastapi import FastAPI, Request
from mangum import Mangum
from fastapi.responses import JSONResponse
import uvicorn
from typing import Union
import yaml

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def read_root():
   return {"Welcome to": "My first FastAPI depolyment using Docker image"}

@app.get("/api/resources")
def read_root():
   return {"Api-Resources"}

@app.get("/api/resources")
async def read_resources(request: Request):
    # Read the YAML file contents
    with open("data/ebbcarbon.yaml", "r") as yaml_file:
        data = yaml.safe_load(yaml_file)

    # Return the resources
    return JSONResponse({"result": data})

@app.get("/{text}")
def read_item(text: str):
   return JSONResponse({"result": text})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
   return JSONResponse({"item_id": item_id, "q": q})

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8080)