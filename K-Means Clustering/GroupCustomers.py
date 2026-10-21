from sklearn.cluster import KMeans

X = [[10], [12], [15], [80], [85], [90]]

model = KMeans(n_clusters=2, random_state=42, n_init=10)
model.fit(X)

print("Customer groups:", model.labels_)
