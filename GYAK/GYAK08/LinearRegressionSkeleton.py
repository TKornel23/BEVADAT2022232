import numpy as np


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        ...

    def fit(self, X: np.array, y: np.array):
        ...

    def predict(self, X):
        ...
