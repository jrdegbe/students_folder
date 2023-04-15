import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

st.title("Student Performance Predictor")

# Collect input from the user
gender = st.selectbox("Gender", ["male", "female"])
race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_level_of_education = st.selectbox("Parental Level of Education", ["some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"])
lunch = st.selectbox("Lunch", ["free/reduced", "standard"])
test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])

# Send data to FastAPI backend and display the result
if st.button("Predict Average Score"):
    data = {
        "gender": gender,
        "race/ethnicity": race_ethnicity,
        "parental level of education": parental_level_of_education,
        "lunch": lunch,
        "test preparation course": test_preparation_course
    }
    response = requests.post(f"{FASTAPI_URL}/predict", json=data)
    prediction = response.json()["predicted_average_score"]
    st.write(f"Predicted Average Score: {prediction:.2f}")
