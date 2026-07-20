# 🤖 AI Resume Analyzer & Interview Preparation Assistant

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 📌 Overview

AI Resume Analyzer & Interview Preparation Assistant is an intelligent web application that analyzes resumes using Large Language Models (LLMs) and provides detailed, actionable feedback to help job seekers improve their resumes and prepare for interviews.

The application extracts text from PDF resumes, evaluates resume quality, identifies strengths and weaknesses, categorizes technical skills, calculates a resume score, and generates personalized interview questions based on the uploaded resume.

---

## 🚀 Live Demo

🔗 **Application:** https://resume-analyzer-interview-assistant.streamlit.app/

---

# ✨ Features

✅ Upload PDF Resume

✅ AI-powered Resume Analysis

✅ Resume Score (0–100)

✅ Technical Skill Categorization

✅ Strength Analysis

✅ Weakness Detection

✅ Missing Skill Identification

✅ Resume Improvement Suggestions

✅ Hiring Assessment

✅ AI Interview Question Generator

- HR Questions
- Technical Questions
- Resume-Based Questions

---

## Home

![Home](screenshots/Home.png)

## Resume Analysis

![Resume Analysis](screenshots/analysis.png)

## Interview Questions

![Interview Questions](screenshots/interview.png)

## Dashboard

![Dashboard](screenshots/upload.png)

# 🛠 Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### AI Model

- Groq API
- Llama 3.1 8B Instant

### Libraries

- PyMuPDF
- Pydantic
- ReportLab
- Pandas
- Python Dotenv

---

# ⚙️ Project Architecture

```
User
      │
      ▼
Upload Resume (PDF)
      │
      ▼
Resume Extraction (PyMuPDF)
      │
      ▼
Resume Analyzer
      │
      ▼
Groq LLM
      │
      ▼
Resume Analysis
      │
      ├────────► Resume Score
      ├────────► Skill Categories
      ├────────► Strengths
      ├────────► Weaknesses
      ├────────► Missing Skills
      ├────────► Suggestions
      └────────► Hiring Assessment
                    │
                    ▼
Interview Question Generator
                    │
                    ▼
HR Questions
Technical Questions
Resume-Based Questions
```

---

# 📂 Project Structure

```
Resume-Analyzer-Interview-Assistant/

│

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

│

├── src/

│   ├── models/

│   ├── prompts/

│   ├── schemas/

│   ├── services/

│   └── utils/

│

└── tests/

```

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/Sourabhnamdev9981/Resume-Analyzer-Interview-Assistant.git
```

Go into the project

```bash
cd Resume-Analyzer-Interview-Assistant
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```
GROQ_API_KEY=your_api_key
```

---

# ▶️ Run Locally

```bash
streamlit run app.py
```

---

# 🎯 Current Features

| Feature | Status |
|----------|--------|
| Resume Upload | ✅ |
| Resume Parsing | ✅ |
| Resume Analysis | ✅ |
| Resume Score | ✅ |
| Skill Categorization | ✅ |
| Strength Detection | ✅ |
| Weakness Detection | ✅ |
| Missing Skills | ✅ |
| Hiring Assessment | ✅ |
| Interview Question Generation | ✅ |

---

# 🔮 Future Improvements

- ATS Resume Matching
- Job Description Comparison
- Resume PDF Report
- Multi-language Resume Support
- Resume Keyword Optimization
- Cover Letter Generator
- AI Career Suggestions
- Resume Version Comparison

---

# 🤝 Contributing

Contributions are welcome!

Feel free to fork this repository, create a feature branch, and submit a pull request.

---

# 👨‍💻 Author

### Sourabh Namdev

Artificial Intelligence & Machine Learning Undergraduate

🔗 GitHub

https://github.com/Sourabhnamdev9981

🔗 LinkedIn

https://www.linkedin.com/in/sourabh-namdev-990515279

---

## ⭐ If you like this project, don't forget to star the repository!
