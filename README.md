AI Resume Analyzer & ATS Scorer

An AI-powered Resume Analyzer that evaluates resumes against job descriptions, calculates ATS (Applicant Tracking System) scores, extracts skills, identifies missing keywords, and provides personalized improvement suggestions.

Features
Upload resumes in PDF format
ATS score calculation
Skill extraction using NLP
Missing keyword detection
Job-role matching
Resume improvement suggestions
Detailed resume analysis report

Tech Stack
Python
NLTK
spaCy
Scikit-learn
Streamlit
PDF Parsing (PyPDF2/pdfplumber)

Installation
Clone the repository:

git clone https://github.com/AbhinavK-tech/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer

Install dependencies:

pip install -r requirements.txt

Download spaCy model

python -m spacy download en_core_web_sm

Run the application:

streamlit run app.py

How It Works:

Upload your resume (PDF).
Enter or upload a job description.
The system analyzes the resume using NLP techniques.
ATS score is generated.
Missing keywords and skills are identified.
Suggestions are provided to improve resume quality.

Use Cases
Students preparing for internships
Job seekers optimizing resumes
Recruiters performing quick resume screening
Career guidance and resume review
