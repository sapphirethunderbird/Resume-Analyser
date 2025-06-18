import re

# Define expected sections and keywords
EXPECTED_SECTIONS = ["experience", "education", "projects", "skills"]
KEYWORDS = [
    "python",
    "machine learning",
    "data",
    "tensorflow",
    "pandas",
    "sql",
    "aws",
    "nlp",
    "deep learning",
]
SOFT_SKILLS = ["communication", "leadership", "team", "collaboration", "initiative"]


def generate_advice(resume_text: str) -> list[str]:
    advice = []

    word_count = len(resume_text.split())
    if word_count < 150:
        advice.append(
            f"Resume is quite short ({word_count} words). Consider elaborating on your experience or skills."
        )

    lower_text = resume_text.lower()

    # Check for key sections
    for section in EXPECTED_SECTIONS:
        if section not in lower_text:
            advice.append(f"Missing expected section: '{section.title()}'.")

    # Check for technical keywords
    missing_keywords = [kw for kw in KEYWORDS if kw not in lower_text]
    if missing_keywords:
        advice.append(
            f"Consider including relevant technical keywords: {', '.join(missing_keywords[:5])}..."
        )

    # Check for soft skills
    found_soft_skills = [s for s in SOFT_SKILLS if s in lower_text]
    if len(found_soft_skills) < 2:
        advice.append(
            "Include more soft skills (e.g., teamwork, leadership, communication)."
        )

    # Bonus: check use of bullet points (a formatting hint)
    bullet_points = re.findall(r"[\n\-•]", resume_text)
    if len(bullet_points) < 5:
        advice.append(
            "Consider using bullet points to organize your responsibilities and achievements more clearly."
        )

    if not advice:
        advice.append("Your resume looks great! No major improvements suggested.")

    return advice
