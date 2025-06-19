import argparse
import os

import joblib

MODEL_PATH = "models/resume_classifier.pkl"
VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"


def predict_resume_category(resume_path):
    # Load model and vectorizer
    clf = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    # Load resume text
    with open(resume_path, "r", encoding="utf-8") as f:
        resume_text = f.read()

    # Transform and predict
    X = vectorizer.transform([resume_text])
    prediction = clf.predict(X)[0]

    return prediction


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--resume", type=str, required=True, help="Path to the .txt resume file"
    )
    args = parser.parse_args()

    if not os.path.exists(args.resume):
        print(f"❌ Resume file not found: {args.resume}")
        exit(1)

    category = predict_resume_category(args.resume)
    print(f"✅ Predicted resume category: **{category}**")
