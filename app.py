import streamlit as st
import pandas as pd
import pickle


# Load the model
with open("house_price_model.pkl", "rb") as f:
    model, input_columns = pickle.load(f)

st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title("🏡 Indian House Price Predictor")
st.markdown("Enter property details below to estimate the price.")

# User inputs
area = st.number_input("Total Area (in sqft)", min_value=100, max_value=10000, value=1200)
bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])
stores = st.selectbox("Stores", [1, 2, 3, 4])

mainroad = st.selectbox("Main Road Access", ['yes', 'no'])
guestroom = st.selectbox("Guest Room", ['yes', 'no'])
basement = st.selectbox("Basement", ['yes', 'no'])
hotwaterheating = st.selectbox("Hot Water Heating", ['yes', 'no'])
airconditioning = st.selectbox("Air Conditioning", ['yes', 'no'])

parking = st.slider("Parking Spaces", 0, 5, 1)
prefarea = st.selectbox("Preferred Area", ['yes', 'no'])
furnishingstatus = st.selectbox("Furnishing Status", ['furnished', 'semi-furnished', 'unfurnished'])

# Predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'stories': stories,
        'mainroad': mainroad,
        'guestroom': guestroom,
        'basement': basement,
        'hotwaterheating': hotwaterheating,
        'airconditioning': airconditioning,
        'parking': parking,
        'prefarea': prefarea,
        'furnishingstatus': furnishingstatus
    }])

    prediction = model.predict(input_df)[0]
        # Lower price using division or subtraction
    adjusted_price = prediction / 4 
    # Ensure it's not negative
    adjusted_price = max(adjusted_price, 0)

    st.success(f"🏷️ Estimated House Price: {int(adjusted_price)}")
