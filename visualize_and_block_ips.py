# visualize_and_block_ips.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os
import subprocess

# -----------------------------
# Find latest CSV from ML-IDS
# -----------------------------
prediction_files = sorted(glob.glob("../new_predictions*.csv"), key=os.path.getmtime)
if not prediction_files:
    raise FileNotFoundError("❌ No prediction CSV file found in ../")
latest_csv = prediction_files[-1]

print(f"📊 Using latest prediction file: {latest_csv}")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv(latest_csv)
print(f"✅ Loaded {len(df)} rows")

# -----------------------------
# Detect prediction column
# -----------------------------
for col in ['Prediction', 'Class', 'Predicted_Label']:
    if col in df.columns:
        pred_col = col
        break
else:
    raise Exception("❌ No prediction column found in CSV!")

# -----------------------------
# Summary
# -----------------------------
summary_counts = df[pred_col].value_counts()
summary_percent = (summary_counts / len(df) * 100).round(2)

print("\n=== Prediction Summary ===")
print(summary_counts)
print("\n=== Prediction Percentages ===")
print(summary_percent)

# -----------------------------
# Visualization
# -----------------------------
plt.figure(figsize=(6,4))
palette = {'BENIGN':'green', 'ATTACK':'red'}
sns.countplot(x=pred_col, data=df, palette=palette)
plt.title("ML-IDS Prediction Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()

chart_file = latest_csv.replace(".csv", "_distribution.png")
plt.savefig(chart_file)
plt.show()
print(f"\n✅ Chart saved as {chart_file}")

# -----------------------------
# IPS Summary: Top attacking IPs
# -----------------------------
top_n_ips = 10
if 'Src IP' in df.columns:
    attacks = df[df[pred_col] != 'BENIGN']
    if len(attacks) > 0:
        top_ips = attacks['Src IP'].value_counts().head(top_n_ips)
        print(f"\n=== Top {top_n_ips} Attacking IPs ===")
        print(top_ips)

        # -----------------------------
        # Block IPs using iptables (requires sudo)
        # -----------------------------
        for ip in top_ips.index:
            cmd = ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"]
            print(f"🔒 Blocking IP: {ip} -> {' '.join(cmd)}")
            # Uncomment the next line to actually block
            # subprocess.run(cmd)
    else:
        print("\nNo attacks detected. No IPs to block.")
else:
    print("\nNo 'Src IP' column found. Skipping IPS summary.")

