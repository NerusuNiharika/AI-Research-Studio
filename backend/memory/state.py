from typing_extensions import TypedDict, Annotated
import operator


class ResearchState(TypedDict):

    # User Input
    topic: str

    # Planner Output
    research_plan: list[str]

    # Research Agent Output
    research_results: Annotated[list[str], operator.add]

    # Reviewer
    reviewer_feedback: str
    approved: bool
    retry_count: int

    # Final Outputs
    summary: str
    report: str
    references: str

    # Generated Files
    report_path: str
    ppt_path: str