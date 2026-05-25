import re

# Clean text
def clean_text(text):

    text = text.lower()

    text = re.sub(r'\n', ' ', text)

    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

    text = re.sub(r'\s+', ' ', text)

    return text


# General skills database
skills_database = [

    # Programming
    "python", "java", "c++", "javascript", "sql",

    # Data Science
    "machine learning", "deep learning", "pandas",
    "numpy", "tensorflow", "pytorch", "power bi",
    "tableau", "excel",

    # Cloud
    "aws", "azure", "gcp", "cloud", "docker",
    "kubernetes", "terraform", "jenkins",

    # Web
    "html", "css", "react", "nodejs", "django",
    "flask",

    # DevOps
    "linux", "git", "github", "devops",

    # Database
    "mysql", "mongodb", "postgresql"
]


# Extract skills
def extract_skills(text):

    found_skills = []

    for skill in skills_database:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return list(set(found_skills))