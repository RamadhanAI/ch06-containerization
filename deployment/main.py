from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.joblib")

@app.post("/predict")
def predict(input_data: dict):
    features = np.array(input_data["data"]).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}