from langchain_core.messages import HumanMessage

from memory.state import ResearchState

from llm import llm
from tools.web_search import web_search_tool
from tools.rag_tool import rag_tool


def research_agent(state: ResearchState) -> ResearchState:

    print("\n========== RESEARCH AGENT ==========")

    state["research_results"] = []

    print(f"Number of Objectives: {len(state['research_plan'])}")

    for i, objective in enumerate(state["research_plan"], start=1):

        print(f"\n========== OBJECTIVE {i} ==========")
        print(objective)

        # -------------------------------
        # WEB SEARCH
        # -------------------------------
        print("\nRunning Web Search...")

        web_results = web_search_tool.invoke(
            {
                "query": objective
            }
        )

        print("✅ Web Search Completed")

        # -------------------------------
        # RAG SEARCH
        # -------------------------------
        print("\nRunning RAG Search...")

        rag_context = rag_tool.invoke(
            {
                "query": objective
            }
        )

        print("✅ RAG Search Completed")

        prompt = f"""
You are an expert research assistant.

Research Objective:
{objective}

Web Search Results:
{web_results}

RAG Context:
{rag_context}

Instructions:
- If RAG Context contains relevant information, use it as the PRIMARY source.
- Use Web Search Results only to supplement missing or recent information.
- Merge both sources into a single coherent summary.
- Do not repeat duplicate information.
- Do not contradict the uploaded PDF unless the web source clearly provides newer facts.
- Write a concise research summary of approximately 120–150 words.
- Focus only on the most important facts.
- End with one short concluding sentence.
"""

        # -------------------------------
        # LLM
        # -------------------------------
        print("\nCalling LLM...")

        response = llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        print("✅ LLM Response Received")

        state["research_results"].append(
            response.content
        )

        print("✅ Research Summary Saved")

    print("\n========== RESEARCH COMPLETED ==========")

    return state