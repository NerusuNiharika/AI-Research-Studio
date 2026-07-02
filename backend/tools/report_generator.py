import os

from docx import Document


def generate_report(report: str, filename: str):

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    document = Document()

    document.add_heading(
        "Research Report",
        level=1
    )

    document.add_paragraph(report)

    document.save(filename)

    return filename