from langchain_core.messages import HumanMessage

from memory.state import ResearchState

from llm import llm


def reviewer_agent(state: ResearchState) -> ResearchState:

    print("\n========== REVIEWER AGENT ==========")

    research_text = "\n\n".join(state["research_results"])
    research_text = research_text[:3000]

    prompt = f"""
You are an expert research reviewer.

Review the following research summaries.

Research:
{research_text}

Instructions:
- If the research is satisfactory, start your response with:
APPROVED

- Otherwise provide at most 3 short bullet points explaining what is missing.

Keep the response under 100 words.
"""

    print("Reviewing Research...")

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    print("Review Completed.")

    feedback = response.content

    state["reviewer_feedback"] = feedback

    state["approved"] = feedback.upper().startswith("APPROVED")

    if not state["approved"]:
        state["retry_count"] += 1
        print(f"Retry Count: {state['retry_count']}")

    return state