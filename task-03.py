import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# ==========================================================
# TASK 03 - FEATURE SELECTION
# Machine Learning Internship - Saiket Systems
# ==========================================================

print("=" * 60)
print("TASK 03 - FEATURE SELECTION")
print("=" * 60)

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

try:
    df = pd.read_csv("Clean_Telco_Customer_Churn.csv")
    print("\nDataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: Clean dataset not found.")
    print("Please complete Task 01 first.")
    exit()

# ----------------------------------------------------------
# Separate Features and Target
# ----------------------------------------------------------

X = df.drop("Churn", axis=1)
y = df["Churn"]

print("Number of Features :", X.shape[1])
print("Number of Records  :", X.shape[0])

# ----------------------------------------------------------
# Train Random Forest Model
# ----------------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# ----------------------------------------------------------
# Feature Importance
# ----------------------------------------------------------

importance = model.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n" + "=" * 60)
print("FEATURE IMPORTANCE RANKING")
print("=" * 60)

print(feature_importance.to_string(index=False))

# ----------------------------------------------------------
# Select Top 10 Features
# ----------------------------------------------------------

top_features = feature_importance.head(10)

print("\nTop 10 Important Features\n")
print(top_features)

# ----------------------------------------------------------
# Save Results
# ----------------------------------------------------------

feature_importance.to_csv(
    "Feature_Importance.csv",
    index=False
)

top_features.to_csv(
    "Top_10_Features.csv",
    index=False
)

print("\nResults saved successfully!")

print("\nGenerated Files:")
print("✔ Feature_Importance.csv")
print("✔ Top_10_Features.csv")

print("\nTASK 03 COMPLETED SUCCESSFULLY")