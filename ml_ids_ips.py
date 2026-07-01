import pandas as pd
import numpy as np
import joblib
import subprocess
import os

print("\n=== ML-IDS + IPS Pipeline ===\n")

# ---------------- CONFIG ---------------- #
# Input CSV for demo
flow_csv = "../dataset/cicids_small.csv"
scaler_file = "../scaler.pkl"
model_file = "../ids_model.pkl"
# ---------------------------------------- #

# 1️⃣ Load dataset
if not os.path.exists(flow_csv) or os.path.getsize(flow_csv) == 0:
    print("Error: CSV file is missing or empty!")
    exit()

data = pd.read_csv(flow_csv)
print("Loaded CSV data shape:", data.shape)

# 2️⃣ Remove any label columns if present
for col in ['Label', 'Class', 'Attack']:
    if col in data.columns:
        data = data.drop(col, axis=1)

# 3️⃣ Load scaler & model
scaler = joblib.load(scaler_file)
model = joblib.load(model_file)

# 4️⃣ Align features with training
expected = scaler.feature_names_in_

# Add missing columns
for col in expected:
    if col not in data.columns:
        data[col] = 0

# Remove extra columns & reorder
data = data[expected]

# Replace inf / NaN
data = data.replace([np.inf, -np.inf], np.nan)
data = data.fillna(0)

# 5️⃣ Predict
data_scaled = scaler.transform(data)
predictions = model.predict(data_scaled)

# Save predictions
output = pd.DataFrame(predictions, columns=["Prediction"])
output.to_csv("new_predictions.csv", index=False)

# Summary
summary = output["Prediction"].value_counts().reset_index()
summary.columns = ["Class", "Count"]
summary.to_csv("prediction_summary.csv", index=False)

print("\n=== Prediction Summary ===")
print(summary)

# 6️⃣ IPS: Block attacker IPs if column exists
if "Src IP" in data.columns:
    attack_ips = data.loc[output["Prediction"] != "BENIGN", "Src IP"].unique()
    print("\nBlocking attacker IPs:", attack_ips)
    for ip in attack_ips:
        try:
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
            print("Blocked:", ip)
        except Exception as e:
            print("Failed to block:", ip, e)
else:
    print("\nNo Src IP column found, skipping IP block...")

print("\n=== ML-IDS + IPS Pipeline Finished ===\n")

