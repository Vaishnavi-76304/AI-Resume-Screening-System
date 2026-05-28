import streamlit as st
import pandas as pd

from src.resume_parser import extract_text_from_pdf
from src.screening import calculate_similarity
from src.utils import clean_text, extract_skills

# Page settings
st.set_page_config(
    page_title="AI Resume Screening System",
    layout="wide"
)

# Title
st.title("AI Resume Screening System")

st.write(
    "Upload resumes and compare them with a Job Description"
)

# Job Description Input
job_description = st.text_area(
    "Enter Job Description",
    height=250
)

# Resume Upload
uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# Button
if st.button("Screen Resumes"):

    # Validation
    if not job_description:
        st.warning("Please enter Job Description")

    elif not uploaded_files:
        st.warning("Please upload resumes")

    else:

        # Clean Job Description
        cleaned_jd = clean_text(job_description)

        resume_texts = []
        resume_names = []
        resume_skills = []

        with st.spinner("Analyzing Resumes..."):

            # Process each resume
            for file in uploaded_files:

                # Extract text
                text = extract_text_from_pdf(file)

                # Clean text
                cleaned_text = clean_text(text)

                # Extract skills
                skills = extract_skills(cleaned_text)

                # Store data
                resume_texts.append(cleaned_text)

                resume_names.append(file.name)

                resume_skills.append(", ".join(skills))

            # Calculate AI similarity
            scores = calculate_similarity(
                cleaned_jd,
                resume_texts
            )

            # Create DataFrame
            results = pd.DataFrame({

                "Resume Name": resume_names,

                "Match Score (%)":
                (scores * 100).round(2),

                "Skills Found":
                resume_skills
            })

            # Sort by score
            results = results.sort_values(
                by="Match Score (%)",
                ascending=False
            )

        # Success message
        st.success("Resume Screening Completed")

        # Show results
        st.subheader("Screening Results")

        st.dataframe(results)

        # Charts
        st.subheader("Resume Ranking")

        chart_data = results.set_index("Resume Name")

        st.bar_chart(chart_data["Match Score (%)"])

        # Best Candidate
        top_candidate = results.iloc[0]

        st.subheader("Best Candidate")

        st.write(
            f"Resume: {top_candidate['Resume Name']}"
        )

        st.write(
            f"Match Score: {top_candidate['Match Score (%)']}%"
        )

        st.write(
            f"Skills: {top_candidate['Skills Found']}"
        )
    