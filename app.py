import streamlit as st
# import pickle
import pandas as pd

# Load trained model
from joblib import load
model = load("model.joblib")

st.set_page_config(page_title="Delivery Delay Predictor")

st.title("🚚 Delivery Delay Risk Predictor")
st.write("Predict whether a delivery is likely to be delayed before dispatch.")

# User inputs
distance = st.number_input("Distance (km)", min_value=0.0, step=0.1)
order_hour = st.number_input("Order Hour (0–23)", min_value=0, max_value=23)
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
load = st.number_input("Delivery Partner Load", min_value=1, step=1)
weather = st.selectbox("Weather Condition", ["Clear", "Rain", "Storm"])

if st.button("Predict Delay"):
    input_df = pd.DataFrame(
        [{
            "distance_km": distance,
            "order_hour": order_hour,
            "traffic_level": traffic,
            "delivery_partner_load": load,
            "weather_condition": weather
        }]
    )

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ High risk of delivery delay")
    else:
        st.success("✅ Delivery likely to be on time")
