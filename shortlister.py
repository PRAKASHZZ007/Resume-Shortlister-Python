import os
import PyPDF2
import docx

# -------- Function to read PDF or DOCX --------
def read_file(file_path):
    text = ""

    if file_path.endswith(".pdf"):
        pdf = open(file_path, "rb")
        reader = PyPDF2.PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
        pdf.close()

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text

    return text.lower()

# -------- Read skills --------
skills = []
with open("skills.txt", "r") as f:
    for line in f:
        skills.append(line.strip().lower())

# -------- Read Job Description (TXT FIX) --------
with open("job_description.txt", "r") as f:
    jd_text = f.read().lower()

jd_skills = []
for skill in skills:
    if skill in jd_text:
        jd_skills.append(skill)

# -------- Process resumes --------
print("\n📄 Resume Shortlisting Results\n")

for resume in os.listdir("resumes"):
    resume_text = read_file("resumes/" + resume)

    matched = 0
    for skill in jd_skills:
        if skill in resume_text:
            matched += 1

    if len(jd_skills) > 0:
        percentage = (matched / len(jd_skills)) * 100
    else:
        percentage = 0

    percentage = round(percentage, 2)

    if percentage >= 60:
        status = "SHORTLISTED ✅"
    else:
        status = "REJECTED ❌"

    print("Resume Name   :", resume)
    print("Skills Match  :", matched, "/", len(jd_skills))
    print("Match %      :", percentage)
    print("Status       :", status)
    print("-" * 35)
