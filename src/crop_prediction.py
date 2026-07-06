# crop_prediction.py
# Project: OptiCrop - Smart Agricultural Production Optimization Engine

# Step 1: Import required libraries
import pandas as pd
import pickle
import numpy as np

# Step 2: Load the trained model
try:
    with open("model/model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    print("Error: Trained model not found. Please ensure 'model/model.pkl' exists.")
    exit()

# Step 3: Create sample user input
# Features: N, P, K, temperature, humidity, ph, rainfall
# Example values can be adjusted based on user/environment input
sample_input = np.array([[90, 42, 43, 20.5, 82.0, 6.5, 202.9]])

# Step 4: Convert input into a pandas DataFrame with proper column names
input_df = pd.DataFrame(sample_input, columns=[
    "N", "P", "K", "temperature", "humidity", "ph", "rainfall"
])

# Step 5: Use the trained model to predict the suitable crop
prediction = model.predict(input_df)

# Step 6: Print the prediction result
print(f"The suggested crop is: {prediction[0]}")
