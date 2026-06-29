import pandas as pd

# Load the skills and courses data
skills_df = pd.read_csv("data/skills.csv")
courses_df = pd.read_csv("data/courses.csv")


def get_recommendations(user_skills):
    """
    Compare user skills with AI Engineer skills
    and recommend missing skills + courses.
    """

    # Change this to another role if needed
    target_role = "AI Engineer"

    # Get all required skills for the target role
    required_skills = skills_df[
        skills_df["Role"] == target_role
    ]["Skill"].tolist()

    # Find missing skills
    missing_skills = []

    for skill in required_skills:
        if skill not in user_skills:
            missing_skills.append(skill)

    # Find recommended courses
    recommended_courses = []

    for skill in missing_skills:
        course = courses_df[
            courses_df["Skill"] == skill
        ]

        if not course.empty:
            recommended_courses.append({
                "skill": skill,
                "course": course.iloc[0]["Course"],
                "platform": course.iloc[0]["Platform"]
            })

    # Project Suggestions
    project_suggestions = [
        "AI Resume Analyzer",
        "Face Mask Detection",
        "House Price Prediction",
        "Movie Recommendation System",
        "Fake News Detection",
        "Customer Churn Prediction",
        "Plant Disease Detection",
        "Handwritten Digit Recognition"
    ]

    return {
        "target_role": target_role,
        "missing_skills": missing_skills,
        "courses": recommended_courses,
        "projects": project_suggestions
    }