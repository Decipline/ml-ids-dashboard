# visualize_ids_simple.py
import pandas as pd
import matplotlib.pyplot as plt

# Load predictions CSV
df = pd.read_csv('new_predictions.csv')

# Detect the prediction column
for col in ['Prediction', 'Class', 'Predicted_Label']:
    if col in df.columns:
        pred_col = col
        break
else:
    raise Exception("No prediction column found in CSV!")

# Print summary
print("=== Prediction Summary ===")
print(df[pred_col].value_counts())

# Plot simple bar chart
df[pred_col].value_counts().plot(kind='bar', color=['green', 'red'])
plt.title("ML-IDS Prediction Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()

