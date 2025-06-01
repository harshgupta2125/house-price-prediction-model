import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Step 2: Load Dataset
df = pd.read_csv("data/Housing.csv")  # Make sure your CSV is in this path
df.head()# Step 3: Preprocess Data

# List of categorical columns to encode
categorical_features = ['mainroad', 'guestroom', 'basement',
                        'hotwaterheating', 'airconditioning',
                        'prefarea', 'furnishingstatus']

# Feature columns (excluding price)
X = df.drop('price', axis=1)

# Target column
y = df['price']

# Column Transformer with OneHotEncoding for categorical columns
column_transformer = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(drop='first'), categorical_features)
    ],
    remainder='passthrough'
)
# Step 4: Create and Train the Model

# Create a pipeline with preprocessor and linear regression model
pipeline = Pipeline(steps=[
    ('preprocessor', column_transformer),
    ('model', LinearRegression())
])

# Split dataset for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
pipeline.fit(X_train, y_train)

print("✅ Model trained successfully.")
# Step 5: Evaluate (optional)
score = pipeline.score(X_test, y_test)
print(f"📊 Model R^2 Score: {score:.4f}")
# Step 6: Save the model
import os

# Create directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save model
with open("models/house_price_model.pkl", "wb") as f:
    pickle.dump((pipeline, X.columns), f)

print("💾 Model saved as models/house_price_model.pkl")
