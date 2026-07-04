from flask import Flask, render_template, request
import os

from utils.pdf_reader import extract_text
from utils.ats import calculate_ats_score

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


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

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    # Save uploaded file
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

    return render_template(
        "result.html",
        score=score,
        matched=sorted(matched),
        missing=sorted(missing)
    )


if __name__ == "__main__":
    app.run(debug=True)