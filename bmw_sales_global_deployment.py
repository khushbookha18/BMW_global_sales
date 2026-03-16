
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("XGBoost_model.pkl")

st.title("BMW Sales Prediction System")

st.write("Enter the details below to predict sales category")

# User Inputs
Year = st.number_input("Year")
Month = st.number_input("Month")
Avg_Price_EUR = st.number_input("Average Price (EUR)")
Revenue_EUR = st.number_input("Revenue (EUR)")
BEV_Share = st.number_input("BEV Share")
Premium_Share = st.number_input("Premium Share")
GDP_Growth = st.number_input("GDP Growth")
Fuel_Price_Index = st.number_input("Fuel Price Index")

# New Inputs for categorical features
Region = st.selectbox("Region", ["Europe","RestOfWorld","USA"])
Model = st.selectbox("Model", ["5 Series","MINI","X3","X5","X7","i4","iX"])

# Create dataframe for prediction
input_data = pd.DataFrame({
    'Year':[Year],
    'Month':[Month],
    'Avg_Price_EUR':[Avg_Price_EUR],
    'Revenue_EUR':[Revenue_EUR],
    'BEV_Share':[BEV_Share],
    'Premium_Share':[Premium_Share],
    'GDP_Growth':[GDP_Growth],
    'Fuel_Price_Index':[Fuel_Price_Index],

    'Region_Europe':[1 if Region=="Europe" else 0],
    'Region_RestOfWorld':[1 if Region=="RestOfWorld" else 0],
    'Region_USA':[1 if Region=="USA" else 0],

    'Model_5 Series':[1 if Model=="5 Series" else 0],
    'Model_MINI':[1 if Model=="MINI" else 0],
    'Model_X3':[1 if Model=="X3" else 0],
    'Model_X5':[1 if Model=="X5" else 0],
    'Model_X7':[1 if Model=="X7" else 0],
    'Model_i4':[1 if Model=="i4" else 0],
    'Model_iX':[1 if Model=="iX" else 0]
})

# Prediction
if st.button("Predict"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("High Sales Expected")
    else:
        st.error("Low Sales Expected")
```
