import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load your data
df = pd.read_csv(r"C:\Users\uz403f\Documents\Scaler\Streamlit\devivenv\cars 24 data.csv")

# Streamlit app
st.title('Car Predictions')

# Function to load and predict using the model
def model_pred(features):
    with open(r"C:\Users\uz403f\Documents\Scaler\Streamlit\devivenv\car_pred_model", "rb") as file:
        model = pickle.load(file)
    # Prediction logic goes here
    return model.predict([features])[0]

# Display dataframe
st.write(df)

# Example inputs for model prediction (these should be taken from user input in a real app)
fuel_encoded = st.number_input('Fuel Encoded', value=1)
transmission_encoded = st.number_input('Transmission Encoded', value=1)
seats = st.number_input('Seats', value=4)
engine = st.number_input('Engine', value=1500)
year = st.number_input('Year', value=2020)
mileage = st.number_input('Mileage', value=10000)
brand_encoded = st.number_input('Brand Encoded', value=2)
model_encoded = st.number_input('Model Encoded', value=3)
some_other_feature = st.number_input('Some Other Feature', value=1)

# Collecting all features into a list
input_features = [fuel_encoded, transmission_encoded, seats, engine, year, mileage, brand_encoded, model_encoded, some_other_feature]

# Get prediction
price = model_pred(input_features)
st.write(f'Predicted price: {price}')
