import pandas as pd
import subprocess

# Read prediction results
df = pd.read_csv("new_predictions.csv")

# Load original traffic file (with IP addresses)
traffic = pd.read_csv("dataset/live_traffic_cic.csv")

# Add predictions
traffic["Prediction"] = df["Prediction"]

# Get attacker IPs
attack_ips = traffic[traffic["Prediction"] != "BENIGN"]["Src IP"].unique()

print("Blocking IPs:", attack_ips)

# Block each IP
for ip in attack_ips:
    try:
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
        print("Blocked:", ip)
    except:
        print("Failed to block:", ip)

