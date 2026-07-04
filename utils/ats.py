from utils.skills import SKILLS


def calculate_ats_score(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    # Extract only technical skills
    resume_skills = set()

    jd_skills = set()

    for skill in SKILLS:

        if skill in resume_text:
            resume_skills.add(skill)

        if skill in job_description:
            jd_skills.add(skill)

    matched_skills = resume_skills.intersection(jd_skills)

    missing_skills = jd_skills - resume_skills

    if len(jd_skills) == 0:
        score = 0
    else:
        score = round((len(matched_skills) / len(jd_skills)) * 100, 2)

    return score, matched_skills, missing_skills