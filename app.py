import pandas as pd
import streamlit as st
import pickle as pk
import numpy as np



model = pk.load(open(r"C:\Users\Saurabh Maurya\Documents\PROJECT OF ML\House_predicrion_model.pkl", "rb"))


st.header("House Price Predictor")
data = pd.read_csv(r"C:\Users\Saurabh Maurya\Documents\PROJECT OF ML\Cleaned_data.csv")




Area = st.number_input("Area(sqft):",min_value=500)
Bedrooms = st.number_input("Number of bedrooms:",min_value=1)
Bathrooms = st.number_input("Number of bathrooms:",min_value=1)
Mainroad = st.selectbox("Near Main Road :?",["yes","no"])
Guestroom = st.selectbox("GuestRoom vailable?",["yes","no"])

input =  pd.DataFrame([[Area, Bedrooms, Bathrooms, Mainroad, Guestroom]],columns=['area', 'bedrooms', 'bathrooms', 'mainroad', 'guestroom'])
if st.button("Predict Price"):
    prediction = model.predict(input)
    price = float(prediction[0])
    st.success(f"House Price:₹{round(price)}")


import pandas as pd




