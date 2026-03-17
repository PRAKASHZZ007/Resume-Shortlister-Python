
import streamlit as st
from shortlister import process_resume

st.title("Mini ATS - Resume Screening")

uploaded_files = st.file_uploader(
    "Upload Multiple Resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success("Resumes Uploaded Successfully")

    for file in uploaded_files:

        matched, total, percentage, status, matched_skills, missing_skills = process_resume(file)

        st.write("------")
        st.write("📄 File:", file.name)
        st.write("Skills Match:", matched, "/", total)
        st.write("Match %:", percentage)
        st.write("Status:", status)

        st.write("✅ Matched Skills:", ", ".join(matched_skills) if matched_skills else "None")
        st.write("❌ Missing Skills:", ", ".join(missing_skills) if missing_skills else "None")