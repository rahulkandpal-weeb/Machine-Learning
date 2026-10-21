from sklearn.tree import DecisionTreeClassifier

# Study hours
X = [[1], [2], [3], [4], [5], [6]]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

prediction = model.predict([[5]])

if prediction[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")
