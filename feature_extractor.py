import pandas as pd

df = pd.read_csv("traffic.csv", names=["src", "dst", "proto", "length"])

df["proto"] = df["proto"].astype(int)
df["length"] = df["length"].astype(int)

df.to_csv("features.csv", index=False)
print("[+] Features saved to features.csv")

