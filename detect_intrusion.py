import pandas as pd
import joblib
import numpy as np

print("\n=== ML IDS Intrusion Detection ===\n")

# Load trained model and scaler
model = joblib.load("ids_model.pkl")
scaler = joblib.load("scaler.pkl")

# Load new data
data = pd.read_csv("dataset/cicids_small.csv")
print("Loaded data shape:", data.shape)

# ---------------- CLEAN + ALIGN ---------------- #

# Remove label column if present
for col in ['Label', 'Class', 'Attack']:
    if col in data.columns:
        data = data.drop(col, axis=1)

# Expected features from training
expected = scaler.feature_names_in_

# Add missing columns
for col in expected:
    if col not in data.columns:
        data[col] = 0

# Remove extra columns & reorder
data = data[expected]

# Replace infinity & very large values
data = data.replace([np.inf, -np.inf], np.nan)

# Fill NaN with 0
data = data.fillna(0)

print("Data aligned to model features:", data.shape)

# ------------------------------------------------ #

# Scale features
data_scaled = scaler.transform(data)

# Predict
predictions = model.predict(data_scaled)

# Save predictions
output = pd.DataFrame(predictions, columns=["Prediction"])
output.to_csv("new_predictions.csv", index=False)

# Create summary
summary = output["Prediction"].value_counts().reset_index()
summary.columns = ["Class", "Count"]
summary.to_csv("prediction_summary.csv", index=False)

print("\n=== Prediction Summary ===")
print(summary)
print("\nSaved: new_predictions.csv & prediction_summary.csv")

