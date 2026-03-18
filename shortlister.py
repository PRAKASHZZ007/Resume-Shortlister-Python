
import PyPDF2
import docx


# -------- Function to read PDF or DOCX --------
def read_file(file):
    text = ""

    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    elif file.name.endswith(".docx"):
        doc = docx.Document(file)

        for para in doc.paragraphs:
            text += para.text

    return text.lower()


# -------- Main Function --------
def process_resume(uploaded_file):

    # -------- Read requirements --------
    requirements = []

    with open("requirements_skills.txt", "r") as f:
        for line in f:
            requirements.append(line.strip().lower())

    # -------- Resume text --------
    resume_text = read_file(uploaded_file)

    matched_skills = []
    missing_skills = []

    for skill in requirements:
        if skill in resume_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    matched = len(matched_skills)
    total = len(requirements)

    if total > 0:
        percentage = (matched / total) * 100
    else:
        percentage = 0

    percentage = round(percentage, 2)

    if percentage >= 60:
        status = "SHORTLISTED ✅"
    else:
        status = "REJECTED ❌"

    return matched, total, percentage, status, matched_skills, missing_skills