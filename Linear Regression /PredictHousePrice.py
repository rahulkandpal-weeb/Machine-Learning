from sklearn.linear_model import LinearRegression
X = [[500], [1000], [1500], [2000]]
y = [10, 20, 30, 40]
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[1200]])
print("Predicted house price:", prediction[0], "lakhs")
