# Resume Analyzer & Interview Preparation Assistant

An AI-powered Resume Analyzer and Interview Preparation Assistant built using **Python, Streamlit, and Google's Gemini API**. The application analyzes resumes, identifies strengths and weaknesses, provides improvement suggestions, performs skill-gap analysis, predicts ATS compatibility, and generates personalized interview questions.

---

## Features

### Resume Analysis

* Upload PDF resumes
* Extract and process resume content
* Analyze:

  * Skills
  * Projects
  * Education
  * Experience
  * Strengths
  * Weaknesses

### Resume Scoring

* Overall resume score
* Section-wise evaluation
* Improvement recommendations

### Skill Gap Analysis

* Identify missing skills
* Recommend learning paths
* Compare current profile against target roles

### Interview Preparation

* Personalized HR questions
* Personalized Technical questions
* Resume-based interview questions

### ATS Analysis

* ATS compatibility score
* Keyword analysis
* Missing keyword suggestions

### Report Generation

* Comprehensive analysis report
* Downloadable PDF report

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini API

### PDF Processing

* PyMuPDF

### Data Validation

* Pydantic

### Report Generation

* ReportLab

---

## Project Architecture

Resume Upload
↓
PDF Text Extraction
↓
Resume Parsing
↓
Gemini Analysis Engine
├── Resume Analysis
├── Resume Scoring
├── Skill Gap Analysis
├── ATS Analysis
└── Interview Question Generation
↓
PDF Report Generator
↓
Downloadable Report

---

## Folder Structure

```text
Resume-Analyzer-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── assets/
├── data/
│   └── reports/
│
├── src/
│   ├── config/
│   ├── models/
│   ├── services/
│   └── utils/
│
├── tests/
└── screenshots/
```

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/resume-analyzer-interview-assistant.git

cd resume-analyzer-interview-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## Future Enhancements

* Job Description Matching
* Resume Tailoring for Specific Roles
* AI Career Roadmap Generation
* Mock Interview Simulation
* Voice-Based Interview Practice
* Multi-Resume Comparison
* Resume Version Tracking

---

## Learning Outcomes

* Generative AI Application Development
* Prompt Engineering
* Document Processing
* Streamlit Application Development
* Gemini API Integration
* Software Architecture Design
* ATS Optimization Techniques
* Production-Level Python Development

---

## Resume Description

**Resume Analyzer & Interview Preparation Assistant | Python, Streamlit, Gemini API**

* Developed an AI-powered resume analysis platform using Gemini API to evaluate skills, projects, education, and experience.
* Implemented resume scoring, ATS analysis, skill-gap detection, and personalized interview question generation.
* Built a modular, deployment-ready Streamlit application with PDF report generation capabilities.
* Applied Generative AI, prompt engineering, and document processing techniques to deliver career-readiness insights.
