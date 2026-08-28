import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X, y = iris.data, iris.target

model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)

joblib.dump(model, "model.joblib")
print("Model saved!")
