from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def create_pdf_report(filename, score, matched, missing):
    pdf = SimpleDocTemplate(filename, pagesize=letter)

    elements = []

    elements.append(
        Paragraph("<b>AI Resume Analyzer Report</b>", styles["Title"])
    )

    elements.append(
        Paragraph(f"<b>ATS Score:</b> {score:.2f}%", styles["Heading2"])
    )

    data = [["Matched Skills", "Missing Skills"]]

    matched = list(matched)
    missing = list(missing)

    max_rows = max(len(matched), len(missing))

    while len(matched) < max_rows:
        matched.append("")

    while len(missing) < max_rows:
        missing.append("")

    for i in range(max_rows):
        data.append([matched[i], missing[i]])

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (0, -1), colors.lightgreen),
        ("BACKGROUND", (1, 1), (1, -1), colors.pink),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ]))

    elements.append(table)

    pdf.build(elements)