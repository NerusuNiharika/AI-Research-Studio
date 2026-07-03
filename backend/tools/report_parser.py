import re


def parse_report(report: str):

    report = report.strip()

    title = ""

    sections = []

    current_title = None
    current_content = []

    lines = report.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # -----------------------------
        # Main Title
        # -----------------------------

        if line.startswith("# ") and not line.startswith("##"):

            title = line.replace("#", "").strip()
            continue

        # -----------------------------
        # Section Heading
        # -----------------------------

        if line.startswith("## "):

            if current_title is not None:

                sections.append(
                    {
                        "title": current_title,
                        "content": "\n".join(current_content).strip()
                    }
                )

            current_title = line.replace("##", "").strip()

            current_content = []

            continue

        # -----------------------------
        # Section Content
        # -----------------------------

        current_content.append(line)

    # Last Section

    if current_title is not None:

        sections.append(
            {
                "title": current_title,
                "content": "\n".join(current_content).strip()
            }
        )

    # Remove Empty Sections

    sections = [

        section

        for section in sections

        if section["content"].strip()

    ]

    return {

        "title": title,

        "sections": sections

    }