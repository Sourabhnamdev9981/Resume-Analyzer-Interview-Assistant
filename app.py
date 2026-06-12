import streamlit as st

from src.services.resume_service import process_resume
from src.services.resume_analyzer import analyze_resume

st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 Resume Analyzer & Interview Preparation Assistant")

st.write("Upload your resume and receive AI-powered analysis.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    result = process_resume(uploaded_file)

    st.success("Resume uploaded successfully!")

    with st.expander("View Extracted Resume Text"):
        st.text_area("Resume Content", result["resume_text"], height=300)

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            analysis = analyze_resume(result["resume_text"])

        st.success("Analysis Complete")

        st.metric("Resume Score", f"{analysis.resume_score}/100")

        st.progress(analysis.resume_score / 100)
        col1, col2 = st.columns(2)

        with col1:

            st.subheader("💪 Strengths")

            for strength in analysis.strengths:
                st.write(f"• {strength}")

        with col2:

            st.subheader("⚠️ Weaknesses")

            for weakness in analysis.weaknesses:
                st.write(f"• {weakness}")

        st.subheader("🛠 Missing Skills")

        for skill in analysis.missing_skills:
            st.write(f"• {skill}")

        st.subheader("📈 Improvement Suggestions")

        for suggestion in analysis.improvement_suggestions:
            st.write(f"• {suggestion}")

        st.subheader("🎯 Hiring Assessment")

        st.info(analysis.hiring_assessment)

        st.subheader("🧠 Skill Categories")

        for category, skills in analysis.skill_categories.items():

            if skills:

                st.markdown(f"**{category} ({len(skills)})**")

                st.caption(" • ".join(skills))
