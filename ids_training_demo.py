import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

# Generate dummy dataset
data = pd.DataFrame({
    "feature1": range(100),
    "feature2": [x*2 for x in range(100)],
    "Label": [0 if x < 50 else 1 for x in range(100)]
})

X = data[["feature1", "feature2"]]
y = data["Label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Plot features
plt.scatter(data["feature1"], data["feature2"], c=data["Label"])
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Dummy IDS Dataset")
plt.show()
