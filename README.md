# 🏡 House Price Prediction Web App (India)

A simple and fast web application built using **Streamlit** that predicts house prices in India based on input features like area, bedrooms, bathrooms, and amenities.

---

## 🚀 Features

- Predicts house prices using a trained machine learning model.
- Clean and fast HTML form-based UI.
- Estimates price in Indian Rupees (₹).
- Lightweight — built without Streamlit.
- Can be deployed on Heroku, Render, or any cloud service.

---

## 📊 Model Details

- **ML Model:** Linear Regression
- **Libraries:** `scikit-learn`, `pandas`, `numpy`, `streamlit`
- **Trained on:** Real housing dataset with features like:
  - Area (sqft)
  - Number of bedrooms
  - Bathrooms
  - Stories
  - Amenities (air conditioning, parking, etc.)

---

## 🏗️ Project Structure

```
house-price-prediction-model/
│
├── models/
│   └── house_price_model.pkl      # Trained ML model
│
├── data/
│   └── Housing.csv
├── house_price_predicton.ipynb    # Exploratory Data Analysis
│
├── app.py                        # Streamlit application
├── requirements.txt              # Project dependencies
└── README.md                     # Project overview
```

---

## 💻 Installation & Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/house-price-prediction-model.git
cd house-price-prediction-model
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app


```bash
streamlit run app.py
```

Then open your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

---

## 📄 License

This project is licensed under the MIT License.