from typing import List

import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("model.joblib")


class PredictRequest(BaseModel):
    data: List[float]


@app.post("/predict")
def predict(request: PredictRequest):
    prediction = model.predict([request.data])
    return {"class_index": int(prediction[0])}
