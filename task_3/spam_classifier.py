import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ---------------------------------------------------------
# 1. Create or load dataset
# ---------------------------------------------------------

# A small built-in dataset for the exam (you can also upload your own)
data = {
    "text": [
        "Congratulations! You won a free iPhone. Click here to claim.",
        "URGENT! Your bank account is locked. Verify immediately.",
        "Win $5000 now by entering this contest!",
        "Hey, are you free for a call tomorrow?",
        "Don't forget our meeting at 5 PM.",
        "Can you send me the report from yesterday?",
        "Limited-time offer!! Buy 1 get 2 free!!!",
        "Your Amazon package has been shipped.",
        "Join our cybersecurity webinar today!",
        "Claim your discount by clicking this link now!"
    ],
    "label": [
        "spam", "spam", "spam",
        "ham", "ham", "ham",
        "spam", "ham", "ham", "spam"
    ]
}

df = pd.DataFrame(data)

# Save dataset so it is visible in GitHub
df.to_csv("sample_dataset.csv", index=False)

print("Dataset sample:")
print(df.head())

# ---------------------------------------------------------
# 2. Preprocessing
# ---------------------------------------------------------

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42
)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words="english")
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# ---------------------------------------------------------
# 3. Model training
# ---------------------------------------------------------

model = LogisticRegression()
model.fit(X_train_vectors, y_train)

# ---------------------------------------------------------
# 4. Evaluation
# ---------------------------------------------------------

predictions = model.predict(X_test_vectors)

accuracy = accuracy_score(y_test, predictions)
print("\nModel Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, predictions))

cm = confusion_matrix(y_test, predictions)
print("\nConfusion Matrix:")
print(cm)

# Plot confusion matrix
plt.imshow(cm, cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
plt.show()
