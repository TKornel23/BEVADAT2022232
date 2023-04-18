import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class LinearRegression:
    def __init__(self, dataset: pd.DataFrame, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr
        self.dataset = dataset

    def fit(self, X: np.array, y: np.array):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Building the model
        m = 0
        c = 0

        self.L = 0.2 # The learning Rate
        self.epochs = 1000 # The number of iterations to perform gradient descent

        n = float(len(self.x_train)) # Number of elements in X

        # Performing Gradient Descent 
        losses = []
        for i in range(self.epochs):
            y_pred = m * self.x_train + c # The current predicted value of Y

            residuals = y_pred - self.y_train
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(self.x_train * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            self.m = m + self.L * D_m  # Update m
            self.c = c + self.L * D_c  # Update c
        
        return self.x_train, self.y_train

    def predict(self, X):
        pred = []
        for self.X in self.x_test:
            self.y_pred = self.m*X + self.c
            pred.append(self.y_pred)

        self.y_pred = self.m*self.x_test + self.c
        return self.y_pred
