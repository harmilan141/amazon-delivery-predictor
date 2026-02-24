import streamlit as st

st.set_page_config(page_title="Amazon Delivery Predictor", layout="centered")

st.title("🚚 Amazon Delivery Delay Predictor")

st.write("Welcome to the Amazon Delivery Prediction App!")

delivery_condition = st.selectbox("Delivery Condition (0=Normal, 1=Urgent)", [0, 1])
agent_rating = st.slider("Agent Rating", 1.0, 5.0, 4.0)
agent_age = st.slider("Agent Age", 18, 60, 30)
processing_time = st.slider("Processing Time (minutes)", 5, 120, 30)
distance = st.slider("Distance (km)", 1, 50, 10)
order_hour = st.slider("Order Hour (0-23)", 0, 23, 12)
peak_hour = st.selectbox("Peak Hour (0=No, 1=Yes)", [0, 1])

if st.button("Predict Delivery Status"):
    st.success("Prediction feature will be added soon!")