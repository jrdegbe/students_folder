from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# Load the trained model
with open("student_performance_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.post("/predict")
async def predict_performance(data: dict):
    data = pd.DataFrame([data])
    prediction = model.predict(data)[0]
    return {"predicted_average_score": prediction}
 