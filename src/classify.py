import pickle

from sentence_transformers import LogisticRegression
from sklearn.feature_extraction.text import TfidVectorizer

vectorizer = TfidVectorizer(max_features=1000)
classifier = LogisticRegression()


def train_classifier(texts, labels):
    X = vectorizer.fit_transform(texts)
    classifier.fit(X, labels)
    with open("models/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    with open("models/classifier.pkl", "wb") as f:
        pickle.dump(classifier, f)


def predict(text):
    X = vectorizer.transform([text])
    return classifier.predict(X)
