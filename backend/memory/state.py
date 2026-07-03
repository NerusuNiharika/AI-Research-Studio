from typing_extensions import TypedDict, Annotated
import operator


class ResearchState(TypedDict):

    # User Input
    topic: str

    # Planner Output
    research_plan: list[str]

    # Research Results
    research_results: Annotated[list[str], operator.add]

    # Reviewer
    reviewer_feedback: str

    approved: bool

    retry_count: int

    # Final Report
    report: str

    summary: str

    references: str

    # Parsed Report Sections
    sections: list
    hero: dict

    # Images
    images: dict

    # Generated Files
    report_path: str

    ppt_path: str