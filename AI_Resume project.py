
def candidate_details():
    name = input("Enter Name: ")
    clg = input("Enter College name: ")
    branch = input("Enter Branch: ")
    cgpa = float(input("Enter CGPA: "))
    
    print("\nCandidate details stored successfully")
    return {"name": name, "clg": clg, "branch": branch, "cgpa": cgpa}


def skills():
    skills = input("\nEnter Skills (comma separated): ").split(",")
    skills = [s.strip().lower() for s in skills]  # clean up
    print("\nSkills saved")
    return skills


def experience():
    experience = input("\nEnter Experience: ")
    print("\nExperience saved")
    return experience


def ats_score(candidate_skills, required_skills):
    required_skills = [s.strip().lower() for s in required_skills.split(",")]
    matched = set(candidate_skills) & set(required_skills)
    score = (len(matched) / len(required_skills)) * 100
    print(f"\nATS Score: {score:.2f}%")
    print(f"Matched Skills: {', '.join(matched)}")


# ---- Run the program ----
details = candidate_details()
candidate_skills = skills()
experience_info = experience()
required = input("\nEnter Required Skills (comma separated): ")

ats_score(candidate_skills, required)
