
import streamlit as st
import pandas as pd
import joblib

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("XGBoost_model.pkl")

model = load_model()

st.title("BMW Sales Prediction System")
st.write("Enter the details below to predict sales category")

# Numeric Inputs
Year = st.number_input("Year", min_value=2000, max_value=2035, step=1)
Month = st.number_input("Month", min_value=1, max_value=12, step=1)
Avg_Price_EUR = st.number_input("Average Price (EUR)")
Revenue_EUR = st.number_input("Revenue (EUR)")
BEV_Share = st.number_input("BEV Share")
Premium_Share = st.number_input("Premium Share")
GDP_Growth = st.number_input("GDP Growth")
Fuel_Price_Index = st.number_input("Fuel Price Index")

# Categorical Inputs
Region = st.selectbox("Region", ["Europe", "RestOfWorld", "USA"])
Model = st.selectbox("Model", ["5 Series", "MINI", "X3", "X5", "X7", "i4", "iX"])

# Prediction Button
if st.button("Predict"):

    # Create input dataframe with all required features
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
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("High Sales Expected")
    else:
        st.error("Low Sales Expected")

