from sklearn.linear_model import LinearRegression

# Training data: house size (sq. ft.)
X = [[500], [1000], [1500], [2000]]

# House prices (in lakhs)
y = [10, 20, 30, 40]

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Predict price for a 1200 sq. ft. house
prediction = model.predict([[1200]])

print("Predicted house price:", prediction[0], "lakhs")
