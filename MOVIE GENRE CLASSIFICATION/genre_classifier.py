import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('movies.csv')  # Ensure this file is in the same directory
print("Sample data:")
print(data.head())

# Drop any rows with missing values
data.dropna(subset=['plot', 'genre'], inplace=True)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    data['plot'], data['genre'], test_size=0.2, random_state=42)

# Convert text to TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a logistic regression classifier
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# Make predictions
y_pred = model.predict(X_test_tfidf)

# Evaluation
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Optional: Show top features per genre
def show_top_features(classifier, vectorizer, classes, n=10):
    for i, class_label in enumerate(classes):
        top_features = classifier.coef_[i].argsort()[-n:]
        feature_names = [vectorizer.get_feature_names_out()[j] for j in top_features]
        print(f"\nTop features for {class_label}:")
        print(", ".join(feature_names))

if len(model.classes_) <= 5:  # Prevent overload on too many classes
    show_top_features(model, vectorizer, model.classes_)