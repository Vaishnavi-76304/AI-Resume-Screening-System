## AI Resume Screening System

# AI Resume Screening System

An AI-powered Resume Screening and Ranking System built using Python, Streamlit, NLP, and Sentence Transformers.

The system analyzes resumes against a Job Description (JD) and ranks candidates based on semantic similarity using AI embeddings.

---

# Features

- Upload multiple resumes in PDF format
- Extract text from resumes
- AI-based resume screening
- Semantic similarity matching
- Resume ranking system
- Skills extraction
- Interactive Streamlit dashboard
- Generalized for all job roles
- Real-time match score calculation

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Programming |
| Streamlit | Web Application |
| Sentence Transformers | AI Semantic Matching |
| Scikit-learn | Cosine Similarity |
| pdfplumber | PDF Text Extraction |
| Pandas | Data Handling |
| Conda | Environment Management |

---

# Project Structure

```bash
RESUME_SCREENING/
│
├── app.py
├── setup.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── resume_parser.py
│   ├── screening.py
│   └── utils.py
│
└── resumes/
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Vaishnavi-76304 /AI-Resume-Screening-System.git
```

---

## 2. Move Into Project Folder

```bash
cd AI-Resume-Screening-System
```

---

## 3. Create Conda Environment

```bash
conda create -n resume_screening python=3.11 -y
```

---

## 4. Activate Environment

```bash
conda activate resume_screening
```

---

## 5. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 6. Install Project

```bash
pip install -e .
```

---

# Run The Application

```bash
streamlit run app.py
```

---

# How It Works

## Step 1

Enter Job Description.

Example:

```text
Looking for a Cloud Engineer with AWS, Docker,
Kubernetes, Terraform and Linux experience.
```

---

## Step 2

Upload resumes in PDF format.

---

## Step 3

The AI model converts:

- Job Description
- Resume Content

into semantic embeddings.

---

## Step 4

Cosine similarity calculates the match score.

---

## Step 5

The system ranks resumes from highest to lowest score.

---

# AI Model Used

```text
all-MiniLM-L6-v2
```

This model is provided by Sentence Transformers and helps understand semantic meaning instead of simple keyword matching.

---

# Example Output

| Resume | Match Score |
|---|---|
| cloud_engineer_resume.pdf | 91% |
| devops_resume.pdf | 80% |
| java_developer_resume.pdf | 35% |

---

# Skills Extracted

The system can identify skills such as:

- Python
- AWS
- Azure
- Docker
- Kubernetes
- SQL
- Machine Learning
- Power BI
- React
- DevOps
- Linux
- Terraform

and many more.

---

# Future Improvements

- ATS Score Calculation
- Resume Summarization
- OpenAI/Gemini Integration
- Resume Classification
- Candidate Recommendation
- Database Integration
- Authentication System
- Email Notifications

---

# Advantages

- Faster hiring process
- AI-based smart screening
- Reduces manual effort
- Supports multiple domains
- Better candidate ranking

---

# Author

Vaishnavi Khadse

---

# License

This project is developed for educational and learning purposes.
