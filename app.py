import pdfplumber

resume_skill = ""
# stores the resume skills in a string variable

with pdfplumber.open("resume.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            resume_skill += text + "\n"
            print(text)

skill_db = {

    "Programming": [
        "Python", "Java", "C", "C++", "JavaScript",
        "TypeScript", "Go", "Rust", "Kotlin", "Swift",
        "PHP", "R", "MATLAB"
    ],

    "Web Development": [
        "HTML", "CSS", "Bootstrap", "Tailwind CSS",
        "JavaScript", "React", "Next.js", "Angular",
        "Vue.js", "Node.js", "Express.js", "Flask",
        "Django", "REST API"
    ],

    "Database": [
        "SQL", "MySQL", "PostgreSQL", "SQLite",
        "MongoDB", "Redis", "Oracle", "Firebase"
    ],

    "AI/ML": [
        "Machine Learning", "Deep Learning",
        "TensorFlow", "Keras", "PyTorch",
        "Scikit-learn", "OpenCV", "NLP",
        "Computer Vision", "Generative AI",
        "LLM", "LangChain", "Hugging Face"
    ],

    "Data Science": [
        "NumPy", "Pandas", "Matplotlib",
        "Seaborn", "Plotly", "SciPy",
        "Data Analysis", "Data Visualization",
        "Statistics"
    ],

    "Cloud Computing": [
        "AWS", "Azure", "Google Cloud",
        "EC2", "S3", "Lambda",
        "Cloud Functions"
    ],

    "DevOps": [
        "Docker", "Kubernetes", "Jenkins",
        "Git", "GitHub", "GitLab",
        "CI/CD", "Terraform",
        "Ansible", "Linux"
    ],

    "Cybersecurity": [
        "Network Security", "Ethical Hacking",
        "Penetration Testing", "OWASP",
        "Wireshark", "Burp Suite",
        "Metasploit"
    ],

    "Mobile Development": [
        "Android", "Kotlin", "Java",
        "Flutter", "Dart", "React Native",
        "Swift", "iOS"
    ],

    "Data Engineering": [
        "Apache Spark", "Hadoop",
        "Kafka", "Airflow",
        "ETL", "Data Warehouse"
    ],

    "Testing": [
        "Selenium", "JUnit", "PyTest",
        "Unit Testing", "Automation Testing",
        "Postman"
    ],

    "Operating Systems": [
        "Linux", "Windows",
        "Unix", "Shell Scripting"
    ],

    "Tools": [
        "VS Code", "Jupyter Notebook",
        "Google Colab", "IntelliJ IDEA",
        "Eclipse", "Figma"
    ]
}

found_skills = {}

for category, skills in skill_db.items():

    found_skills[category] = []

    for skill in skills:

        if skill.lower() in resume_text.lower():

            found_skills[category].append(skill)

role_mapping = {
    "ML Engineer": ["AI/ML", "Data Science"],
    "Data Analyst": ["Data Science", "Database"],
    "Python Developer": ["Programming", "Web Development"],
    "DevOps Engineer": ["DevOps", "Cloud Computing"],
    "Full Stack Developer": ["Web Development", "Database"],
    "Cloud Engineer": ["Cloud Computing", "DevOps"]
}
