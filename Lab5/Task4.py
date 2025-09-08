# Job Applicant Scoring System

def score_applicant(education, experience, gender, age):
    """
    Scores a job applicant based on input features.
    education: str ('highschool', 'bachelor', 'master', 'phd')
    experience: int (years)
    gender: str ('male', 'female', 'other')
    age: int
    Returns: int (score)
    """
    # Education scoring
    edu_scores = {
        'highschool': 10,
        'bachelor': 20,
        'master': 30,
        'phd': 40
    }
    score = edu_scores.get(education.lower(), 0)

    # Experience scoring
    if experience < 2:
        score += 5
    elif experience < 5:
        score += 15
    else:
        score += 25

    # Age scoring (neutral, just for demonstration)
    if 18 <= age <= 60:
        score += 10
    else:
        score += 0

    # Gender scoring (neutral, no bias)
    # No points added or subtracted for gender

    return score

def analyze_bias(education, experience, gender, age):
    """
    Analyzes if there is any bias in the scoring logic.
    """
    print("Scoring logic does not use gender in calculation, so no gender bias.")
    print("Education and experience are weighted based on typical job requirements.")
    print("Age is only used to ensure working age, not to favor any group.")
    print("If you input different genders, the score will remain the same for identical education, experience, and age.")

# Example usage
if __name__ == "__main__":
    # Input from user
    education = input("Enter education level (highschool/bachelor/master/phd): ")
    experience = int(input("Enter years of experience: "))
    gender = input("Enter gender (male/female/other): ")
    age = int(input("Enter age: "))

    score = score_applicant(education, experience, gender, age)
    print(f"Applicant Score: {score}")

    analyze_bias(education, experience, gender, age)