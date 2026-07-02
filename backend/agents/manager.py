from memory.state import ResearchState


def manager_agent(state: ResearchState) -> ResearchState:

    print("\n========== MANAGER AGENT ==========")

    if not state["topic"].strip():
        raise ValueError("Research topic cannot be empty.")

    print(f"Topic : {state['topic']}")

    return state