from LinearRegressionSkeleton import LinearRegression
import pandas as pd
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

x = df["petal width (cm)"].values
y = df["sepal length (cm)"].values

linearRegression = LinearRegression(df)

x_test, y_test = linearRegression.fit(x, y)

y_pred = linearRegression.predict(x)

print(linearRegression.evaluate(x, y))

plt.scatter(x_test, y_test)
plt.plot([min(x_test), max(x_test)], [min(y_pred), max(y_pred)], color='red') # predicted
plt.show()