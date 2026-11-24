
#installation: python -m pip install scikit-learn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Naive Bayes model
model = GaussianNB()

# Train model
model.fit(x_train, y_train)

# Predict output
y_pred = model.predict(x_test)

# Calculate accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Predicted values:", y_pred)
print("Actual values:", y_test)