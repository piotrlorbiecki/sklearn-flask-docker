# Load libraries

import pickle
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.externals import

import numpy as np


class Perceptron:

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,y):
                update=self.eta*(target-self.predict(xi))
                self.w_[1:] += update *xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self


    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0, 1, -1)
# Load the iris data
iris = datasets.load_iris()

# Create a matrix, X, of features and a vector, y.
X, y = iris.data, iris.target

# Train a naive logistic regression model
model = Perceptron()
model.fit(X, y)

# Save the trained model as a pickle string.
saved_model = pickle.dumps(model)

# Save the model as a pickle in a file
joblib.dump(model, 'model.pkl')