import glob
import os
import re

import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

DATA_DIR = "data/processed/converted"
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)


def extract_label_from_filename(filename):
    match = re.search(r"resume_\d+_(.+)\.txt", filename)
    return match.group(1).replace("_", " ") if match else "Unknown"


def load_resumes(data_dir):
    texts, labels = [], []
    for path in glob.glob(os.path.join(data_dir, "*.txt")):
        with open(path, "r", encoding="utf-8") as f:
            texts.append(f.read())
            labels.append(extract_label_from_filename(os.path.basename(path)))
    return texts, labels


def main():
    print("🔄 Loading resumes...")
    X_raw, y = load_resumes(DATA_DIR)

    print(f"📄 Loaded {len(X_raw)} resumes across {len(set(y))} categories")

    print("🧹 Vectorizing resumes with TF-IDF...")
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    X = vectorizer.fit_transform(X_raw)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("🤖 Training Logistic Regression model...")
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, y_train)

    print("✅ Training complete. Evaluating model...")
    y_pred = clf.predict(X_test)
    print("🔍 Classification Report:")
    print(classification_report(y_test, y_pred))
    print(f"🎯 Accuracy: {accuracy_score(y_test, y_pred):.2f}")

    print("💾 Saving model and vectorizer to disk...")
    joblib.dump(clf, os.path.join(MODEL_DIR, "resume_classifier.pkl"))
    joblib.dump(vectorizer, os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl"))

    print("🏁 Done!")


if __name__ == "__main__":
    main()
