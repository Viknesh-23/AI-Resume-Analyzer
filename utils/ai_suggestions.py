def generate_suggestions(missing_skills):
    suggestions = []

    skill_tips = {
        "python": "Add more Python projects and highlight Python libraries you have used.",
        "flask": "Include a Flask REST API project in your Projects section.",
        "docker": "Mention Docker containerization and deployment experience.",
        "linux": "Add Linux command-line and server experience.",
        "git": "Mention Git branching, merging and version control workflow.",
        "github": "Include your GitHub profile and project repositories.",
        "rest api": "Mention REST API development using Flask or FastAPI.",
        "sql": "Highlight SQL queries, joins and database design.",
        "mongodb": "Mention MongoDB CRUD operations and Atlas experience.",
        "machine learning": "Include ML projects with Scikit-Learn or TensorFlow.",
        "html": "Mention responsive HTML web pages.",
        "css": "Mention modern CSS and Bootstrap.",
        "javascript": "Highlight JavaScript DOM and API usage."
    }

    for skill in missing_skills:
        key = skill.lower()

        if key in skill_tips:
            suggestions.append(skill_tips[key])
        else:
            suggestions.append(f"Consider adding experience related to {skill}.")

    return suggestions