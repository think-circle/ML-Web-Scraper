from fastapi import FastAPI
from pydantic import BaseModel
import json
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import pandas as pd


app = FastAPI()

class model_input(BaseModel):

    Rooms : float
    Distance : float
    Bathroom : float
    Car : float
    Landsize : float
    BuildingArea : float
    YearBuilt : float
    Lattitude : float
    Longtitude : float
    Propertycount : float


# Loading the saved model
model = tf.keras.models.load_model("models/1/")

@app.get("/hello")
async def hello():
    return f"Welcome"

@app.get("/hello/{name}")
async def hello(name):
    return f"Welcome {name}"


@app.post("/predict")
async def predict(input_parameters : model_input):
    input = input_parameters.json()
    inp_dict = json.loads(input)
    inp_list = list(inp_dict.values())
    X = np.array(inp_list).reshape(1,-1)
    predictions = model.predict(X).tolist()[0][0]
    
    return predictions

    

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)