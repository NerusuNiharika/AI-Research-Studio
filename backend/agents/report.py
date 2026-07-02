from datetime import datetime
import re

from langchain_core.messages import HumanMessage

from memory.state import ResearchState
from llm import llm

from tools.report_generator import generate_report
from tools.ppt_generator import generate_ppt


def report_agent(state: ResearchState) -> ResearchState:

    print("\n========== REPORT AGENT ==========")

    # ----------------------------------------
    # Combine Research Results
    # ----------------------------------------

    research_text = "\n\n".join(state["research_results"])

    research_text = research_text[:5000]

    # ----------------------------------------
    # Prompt
    # ----------------------------------------

    prompt = f"""
You are an expert technical report writer.

Research Topic:
{state["topic"]}

Research Material:
{research_text}

Write a professional research report.

Use the following structure exactly.

# Executive Summary
Write a concise summary (120-150 words).

# Introduction
Introduce the topic.

# Main Findings
Present the important findings clearly using headings or bullet points when appropriate.

# Challenges
Discuss limitations and challenges.

# Future Scope
Explain possible future developments.

# Conclusion
Provide a short conclusion.

# References
List reliable references that support the report.

Rules:
- Use only information from the provided research material.
- Do not invent references.
- If URLs or source names are available in the research material, include them.
- If exact URLs are unavailable, provide source names only.
- Write in professional language.
- Use proper headings.
"""

    print("Generating Final Report...")

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    report = response.content

    print("Report Generated.")

    # ----------------------------------------
    # Executive Summary
    # ----------------------------------------

    summary = ""

    if "# Executive Summary" in report:

        try:

            summary = (
                report.split("# Executive Summary")[1]
                .split("# Introduction")[0]
                .strip()
            )

        except Exception:

            summary = ""

    # ----------------------------------------
    # References
    # ----------------------------------------

    references = ""

    if "# References" in report:

        try:

            references = (
                report.split("# References")[1]
                .strip()
            )

        except Exception:

            references = ""

    # ----------------------------------------
    # Save to State
    # ----------------------------------------

    state["report"] = report
    state["summary"] = summary
    state["references"] = references

    # ----------------------------------------
    # Unique File Names
    # ----------------------------------------

    safe_topic = re.sub(
        r"[^a-zA-Z0-9]+",
        "_",
        state["topic"]
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    report_path = (
        f"reports/{safe_topic}_{timestamp}.docx"
    )

    ppt_path = (
        f"presentations/{safe_topic}_{timestamp}.pptx"
    )

    # ----------------------------------------
    # Generate Files
    # ----------------------------------------

    generate_report(
        report,
        report_path
    )

    generate_ppt(
        state["topic"],
        report,
        ppt_path
    )

    state["report_path"] = report_path
    state["ppt_path"] = ppt_path

    print("Documents Saved Successfully.")

    return state