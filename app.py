from flask import Flask, render_template, request
import os
from resume_parser import extract_text
from skill_matcher import find_skills
from recommendation import get_recommendations
from resume_score import calculate_score

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        return "No file uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Extract text from resume
    resume_text = extract_text(filepath)

    # Find skills
    skills = find_skills(resume_text)

    # Get recommendations
    recommendations = get_recommendations(skills)

    # Calculate score
    score = calculate_score(skills)

    return render_template(
        "result.html",
        score=score,
        skills=skills,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)