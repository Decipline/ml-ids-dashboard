# visualize_and_ips.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# CONFIG
# -----------------------------
csv_file = 'new_predictions.csv'  # Your ML-IDS predictions CSV
chart_file = 'prediction_distribution.png'  # Output chart image
top_n_ips = 10  # Show top N attacking IPs if Src IP exists

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv(csv_file)
print(f"📊 Loaded {len(df)} predictions from {csv_file}")

# -----------------------------
# DETECT PREDICTION COLUMN
# -----------------------------
for col in ['Prediction', 'Class', 'Predicted_Label']:
    if col in df.columns:
        pred_col = col
        break
else:
    raise Exception("❌ No prediction column found in CSV!")

# -----------------------------
# SUMMARY OF PREDICTIONS
# -----------------------------
summary_counts = df[pred_col].value_counts()
summary_percent = (summary_counts / len(df) * 100).round(2)

print("\n=== Prediction Summary ===")
print(summary_counts)
print("\n=== Prediction Percentages ===")
print(summary_percent)

# -----------------------------
# VISUALIZATION
# -----------------------------
plt.figure(figsize=(6,4))
palette = {'BENIGN':'green', 'ATTACK':'red'}
sns.countplot(x=pred_col, data=df, palette=palette)
plt.title("ML-IDS Prediction Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(chart_file)
plt.show()
print(f"\n✅ Chart saved as {chart_file}")

# -----------------------------
# IPS: TOP ATTACKING IPS
# -----------------------------
if 'Src IP' in df.columns:
    attacks = df[df[pred_col] != 'BENIGN']
    if len(attacks) > 0:
        top_ips = attacks['Src IP'].value_counts().head(top_n_ips)
        print(f"\n=== Top {top_n_ips} Attacking IPs ===")
        print(top_ips)
    else:
        print("\nNo attacks detected. No IPs to block.")
else:
    print("\nNo Src IP column found. Skipping IPS summary.")

