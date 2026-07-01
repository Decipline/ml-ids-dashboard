import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("features.csv")[["proto", "length"]]

model = IsolationForest(contamination=0.05)
model.fit(data)

data["anomaly"] = model.predict(data)
data.to_csv("results.csv", index=False)

print("[+] IDS completed. Check results.csv")
