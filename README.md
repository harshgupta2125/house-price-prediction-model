# 🏡 House Price Prediction Web App (India)

A simple and fast web application built using **Flask** that predicts house prices in India based on input features like area, bedrooms, bathrooms, and amenities.

---

## 🚀 Features

- Predicts house prices based on trained machine learning model.
- Clean and fast HTML form-based UI.
- Estimates price in Indian Rupees (₹).
- Lightweight — built without Streamlit.
- Can be deployed on Heroku, Render, or any cloud service.

---

## 📊 Model Details

- ML Model: Linear Regression
- Libraries: `scikit-learn`, `pandas`, `Flask`
- Trained on real housing dataset with features like:
  - Area (sqft)
  - Number of bedrooms
  - Bathrooms
  - Stories
  - Amenities like air conditioning, parking, etc.

---

## 🏗️ Project Structure

house-price-prediction-model/
│
├── models/
│ └── house_price_model.pkl # Trained ML model
│
├── templates/
│ └── index.html # HTML form and result display
│
├── app.py # Flask application
├── requirements.txt # Project dependencies
├── Procfile # For Heroku deployment (optional)
├── runtime.txt # Python version (for Heroku)
└── README.md # Project overview

---

## 💻 Installation & Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/house-price-prediction-model.git
cd house-price-prediction-model
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Flask app
bash
Copy
Edit
python app.py
Then open your browser at http://127.0.0.1:5000/