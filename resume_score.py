def calculate_score(skills):
    """
    Calculate resume score based on number of detected skills.
    """

    total_required_skills = 24

    score = (len(skills) / total_required_skills) * 100

    if score > 100:
        score = 100

    return round(score, 2)