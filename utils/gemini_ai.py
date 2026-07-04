import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# Load .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=API_KEY)


def generate_ai_suggestions(resume_text, job_description):

    prompt = f"""
You are an ATS Resume Expert.

Compare the resume with the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Give exactly 5 resume improvement suggestions.

Rules:
- One suggestion per line.
- Short sentence.
- No numbering.
- No markdown.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        suggestions = []

        for line in text.split("\n"):

            line = (
                line.replace("*", "")
                    .replace("-", "")
                    .strip()
            )

            if line:
                suggestions.append(line)

        return suggestions[:5]

    except Exception as e:

        print("\n========== GEMINI ERROR ==========")
        print(type(e).__name__)
        print(e)
        print("==================================")

        return [
            "Unable to generate AI suggestions right now."
        ]