
from LinearRegressionSkeleton import LinearRegression
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from matplotlib import pyplot as plt
lr = LinearRegression(epochs=20000, lr=0.01)
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
X = df['petal width (cm)'].values
Y = df['sepal length (cm)'].values

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

lr.fit(X_train,y_train)
y_pred = lr.predict(X_test)

plt.scatter(X_test, y_test)
plt.plot([min(X_test), max(X_test)], [min(y_pred),
         max(y_pred)], color='red')  # predicted
plt.show()