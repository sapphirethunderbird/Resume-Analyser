def generate_advice(resume_text):
    advice = []
    if "machine learning" not in resume_text.lower():
        advice.append("Consider adding machine learning experience or tools.")
    if len(resume_text.split()) < 150:
        advice.append("Resume is too short. Add more detailed experiences.")
    return advice
