from langgraph.graph import StateGraph, START, END

from memory.state import ResearchState

from agents.manager import manager_agent
from agents.planner import planner_agent
from agents.research import research_agent
from agents.reviewer import reviewer_agent
from agents.report import report_agent


builder = StateGraph(ResearchState)


builder.add_node("Manager", manager_agent)
builder.add_node("Planner", planner_agent)
builder.add_node("Research", research_agent)
builder.add_node("Reviewer", reviewer_agent)
builder.add_node("Report", report_agent)


builder.add_edge(START, "Manager")
builder.add_edge("Manager", "Planner")
builder.add_edge("Planner", "Research")
builder.add_edge("Research", "Reviewer")


MAX_RETRIES = 2


def review_decision(state: ResearchState):

    if state["approved"]:
        print("\n✅ Research Approved")
        return "Report"

    print(f"Current Retry Count: {state['retry_count']}")

    if state["retry_count"] >= MAX_RETRIES:
        print("\n⚠ Maximum retry limit reached.")
        print("Proceeding to Report Generation...")
        return "Report"

    print("\n🔄 Reviewer requested another research cycle.")
    return "Research"


builder.add_conditional_edges(
    "Reviewer",
    review_decision,
    {
        "Research": "Research",
        "Report": "Report",
    },
)

builder.add_edge("Report", END)

graph = builder.compile()