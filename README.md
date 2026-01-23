# Resume Shortlister (Python)

A simple Python project that automatically shortlists resumes by matching skills with a job description.

## Technologies Used
- Python
- PyPDF2 (to read PDF resumes)
- python-docx (to read DOCX resumes)
- Text files (skills and job description)
- Basic string matching logic

## What This Project Does
This project helps to reduce manual work in resume screening.  
It checks whether a candidate’s resume contains the required skills for a job and gives a match percentage.

## How to Use (Simple Explanation)

1. Add all required job skills in the `skills.txt` file  
   (Example: python, react, sql)

2. Paste the full job description in the `job_description.txt` file

3. Place all candidate resumes (PDF or DOCX) inside the `resumes/` folder

4. Run the Python script:
```bash
python main.py
