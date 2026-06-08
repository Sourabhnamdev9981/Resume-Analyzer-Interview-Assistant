import streamlit as st

from src.services.resume_service import process_resume
from src.services.resume_analyzer import analyze_resume


st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Analyzer & Interview Preparation Assistant")

st.write(
    "Upload your resume and receive AI-powered analysis."
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    result = process_resume(uploaded_file)

    st.success("Resume uploaded successfully!")

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        result["resume_text"],
        height=250
    )

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing resume using Gemini..."):

            analysis = analyze_resume(
                result["resume_text"]
            )

        st.subheader("AI Resume Analysis")

        st.markdown(analysis)