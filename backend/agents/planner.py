from langchain_core.messages import HumanMessage

from memory.state import ResearchState
from llm import llm

def planner_agent(state: ResearchState) -> ResearchState:
    print("\n========== PLANNER AGENT ==========")

    prompt = f"""
You are an expert research planner.

Topic:
{state["topic"]}

Generate EXACTLY 4 research objectives.

Requirements:
- Return exactly 4 objectives.
- Each objective should be one short sentence.
- Cover:
  1. Introduction
  2. Key Concepts / Applications
  3. Challenges / Limitations
  4. Future Scope / Conclusion

Return ONLY the numbered objectives.
Do not add explanations or extra text.
"""

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    plan = []

    for line in response.content.split("\n"):

        line = line.strip()

        if line:

            if "." in line:

                line = line.split(".", 1)[1].strip()

            plan.append(line)

    state["research_plan"] = plan[:4]

    print("\nResearch Objectives:")
    for i, item in enumerate(state["research_plan"], start=1):
        print(f"{i}. {item}")

    return state