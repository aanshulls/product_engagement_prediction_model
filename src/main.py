from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# Load the trained model
model = joblib.load("model.pkl")

# Initialising FastAPI
app = FastAPI()

# Define input data schema
class InputData(BaseModel):
    features: list

# Define the prediction route
@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert list to numpy array
        X = np.array(data.features).reshape(1, -1)
        # Make prediction
        prediction = model.predict(X)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        return {"error": str(e)}

# Root endpoint
@app.get("/")
def home():
    return {"message": "ML Model API is running!"}