# Train and save a classification model
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the data
data = load_breast_cancer()
X, y = data.data, data.target
target_names = data.target_names

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and target names
joblib.dump((model, target_names), 'models/model_breast_cancer.pkl')
print("Model trained and saved.")
