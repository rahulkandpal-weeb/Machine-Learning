## Train-Test Split
Train Test will be implemented later

Train-test splitting divides a dataset into two parts:

- Training set: Used to train the machine learning model.
- Testing set: Used to evaluate the model on unseen data.

Example using scikit-learn:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

