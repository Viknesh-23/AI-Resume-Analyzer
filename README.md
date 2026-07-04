# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python, Flask, Bootstrap, and Google Gemini AI**. It compares a resume with a Job Description (JD), calculates an ATS score, identifies matched and missing skills, and generates AI-powered resume improvement suggestions.

## 🌐 Live Demo

https://ai-resume-analyzer-rqan.onrender.com

## 🚀 Features

- 📄 Upload Resume (PDF)
- 📝 Paste Job Description
- 📊 ATS Score Calculation
- ✅ Matched Skills Detection
- ❌ Missing Skills Detection
- 🤖 AI Resume Suggestions (Google Gemini AI)
- 📈 Interactive Charts (Pie & Bar)
- 📄 Resume Preview
- 📥 Download ATS Report as PDF
- 🌙 Dark Mode
- 📱 Responsive Bootstrap UI

---

## 🛠 Tech Stack

- Python
- Flask
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chart.js
- Google Gemini AI
- PyMuPDF (fitz)
- ReportLab

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── utils/
│   ├── ats.py
│   ├── gemini_ai.py
│   ├── pdf_reader.py
│   ├── pdf_report.py
│   └── skills.py
│
├── uploads/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

```bash
git clone https://github.com/Viknesh-23/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer

pip install -r requirements.txt

python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 📸 Screenshots

### Home Page

(Add screenshot here)

### ATS Result

(Add screenshot here)

---

## 🎯 Future Improvements

- Resume Keyword Highlighting
- Multiple Resume Comparison
- Resume History
- AI Resume Rewrite
- LinkedIn Profile Analysis
- Deploy on Render

---

## 👨‍💻 Author

**Viknesh K**

GitHub: https://github.com/Viknesh-23

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
