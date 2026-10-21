# Email Spam Detection using Naive Bayes

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Training data
emails = [
    "Win a free prize now",
    "Claim your free gift",
    "Congratulations you won money",
    "Let's meet for lunch",
    "Can we discuss the project",
    "Please send me the report"
]

# 1 = Spam, 0 = Not Spam
labels = [1, 1, 1, 0, 0, 0]

# Create a text classification pipeline
model = make_pipeline(
    CountVectorizer(),
    MultinomialNB()
)

# Train the model
model.fit(emails, labels)

# Test with a new email
new_email = ["Congratulations claim your free prize"]

prediction = model.predict(new_email)

if prediction[0] == 1:
    print("Classification: Spam")
else:
    print("Classification: Not Spam")
