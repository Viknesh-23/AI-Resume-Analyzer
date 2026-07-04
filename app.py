from flask import Flask, render_template, request, send_file
import os

from utils.pdf_reader import extract_text
from utils.ats import calculate_ats_score
from utils.pdf_report import create_pdf_report
from utils.ai_suggestions import generate_suggestions

app = Flask(__name__)

# Upload folder configuration
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "resume" not in request.files:
        return "No file uploaded."

    resume = request.files["resume"]

    if resume.filename == "":
        return "No file selected."

    # Save uploaded file
    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(file_path)

    # Extract text from PDF
    resume_text = extract_text(file_path)

    # Get Job Description
    job_description = request.form.get("job_description", "")

    # Calculate ATS Score
    score, matched, missing = calculate_ats_score(
        resume_text,
        job_description
    )

    # Generate AI Suggestions
    suggestions = generate_suggestions(missing)

    # Generate PDF Report
    report_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        "ATS_Report.pdf"
    )

    create_pdf_report(
        report_path,
        score,
        matched,
        missing
    )

    return render_template(
        "result.html",
        score=score,
        matched=sorted(matched),
        missing=sorted(missing),
        suggestions=suggestions,
        report_path="ATS_Report.pdf"
    )


@app.route("/download/<filename>")
def download(filename):
    return send_file(
        os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        ),
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)