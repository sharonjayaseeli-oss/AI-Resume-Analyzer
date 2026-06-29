import pandas as pd

# Load the skills database
skills_df = pd.read_csv("data/skills.csv")

# Get all unique skills from the CSV
ALL_SKILLS = skills_df["Skill"].dropna().unique().tolist()


def find_skills(resume_text):
    """
    Find matching skills from the resume text.
    """

    found_skills = []

    # Convert resume text to lowercase
    resume_text = resume_text.lower()

    # Check each skill
    for skill in ALL_SKILLS:
        if skill.lower() in resume_text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))