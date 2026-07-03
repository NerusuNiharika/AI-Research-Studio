from datetime import datetime
import re

from langchain_core.messages import HumanMessage

from memory.state import ResearchState
from llm import llm

from tools.report_generator import generate_report
from tools.ppt_generator import generate_ppt
from tools.report_parser import parse_report
from tools.image_search import attach_images


def generate_image_query(topic: str, section: str, content: str):

    prompt = f"""
You are an expert at creating image search queries.

Research Topic:
{topic}

Section:
{section}

Section Content:
{content[:500]}

Generate ONE professional image search query.

Rules:
- Maximum 6 words.
- Focus on what should appear in the picture.
- Avoid generic words.
- Do not use punctuation.
- Return ONLY the search query.

Examples

Topic:
AI in Healthcare

Executive Summary

Output:
medical artificial intelligence hospital

----------------------

Topic:
AI in Education

Introduction

Output:
students using AI classroom

----------------------

Topic:
Cybersecurity

Challenges

Output:
cyber security data center
"""

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    return response.content.strip()


def report_agent(state: ResearchState) -> ResearchState:

    print("\n========== REPORT AGENT ==========")

    research_text = "\n\n".join(state["research_results"])

    research_text = research_text[:5000]

    prompt = f"""
You are an expert technical research writer.

Research Topic:
{state["topic"]}

Research Material:
{research_text}

Write a professional research report.

IMPORTANT:

Use proper Markdown formatting.

The report MUST follow this exact structure.

# Research Report: {state["topic"]}

## Executive Summary

Write a concise summary (120-150 words).

## Introduction

Introduce the topic.

## Main Findings

Present the important findings.

IMPORTANT:
Use proper markdown bullet points.

Example:

- Point one

- Point two

- Point three

Do NOT place all points in one paragraph.

## Challenges

Use bullet points whenever possible.

## Future Scope

Use bullet points whenever possible.

## Conclusion

Provide a professional conclusion.

## References

List reliable references.

Rules:

- Use ONLY the provided research material.
- Do not invent references.
- Use professional language.
- Use markdown headings.
"""

    print("Generating Final Report...")

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    report = response.content.strip()

    print("Report Generated.")

    parsed_report = parse_report(report)

    print("Generating Image Queries...")

    enhanced_sections = []

    for section in parsed_report["sections"]:

        query = generate_image_query(

            state["topic"],

            section["title"],

            section["content"]

        )

        print(f"{section['title']} -> {query}")

        section["image_query"] = query

        enhanced_sections.append(section)

    print("Searching Images...")

    report_with_images = attach_images(

        state["topic"],

        enhanced_sections

    )

    summary = ""

    try:

        if "## Executive Summary" in report:

            summary = (

                report.split("## Executive Summary")[1]

                .split("## Introduction")[0]

                .strip()

            )

    except Exception:

        pass

    references = ""

    try:

        if "## References" in report:

            references = (

                report.split("## References")[1]

                .strip()

            )

    except Exception:

        pass

    state["report"] = report

    state["summary"] = summary

    state["references"] = references

    state["sections"] = report_with_images["sections"]

    state["hero"] = report_with_images["hero"]

    state["images"] = report_with_images

    safe_topic = re.sub(

        r"[^a-zA-Z0-9]+",

        "_",

        state["topic"]

    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    report_path = f"reports/{safe_topic}_{timestamp}.docx"

    ppt_path = f"presentations/{safe_topic}_{timestamp}.pptx"

    generate_report(
    report=report,
    hero=report_with_images["hero"],
    sections=report_with_images["sections"],
    filename=report_path
)
    generate_ppt(
    title=state["topic"],
    report=report,
    hero=report_with_images["hero"],
    sections=report_with_images["sections"],
    filename=ppt_path
)

    state["report_path"] = report_path

    state["ppt_path"] = ppt_path

    print("Documents Saved Successfully.")

    return state