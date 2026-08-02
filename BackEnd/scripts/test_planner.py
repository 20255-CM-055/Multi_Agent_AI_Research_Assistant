from agents.planner.planner import PlannerAgent

state = {
    "query": "Agentic AI",
    "research_plan": None,
    "retrieved_documents": None,
    "web_results": None,
    "final_report": None,
    "current_agent": None,
}

planner = PlannerAgent()

updated_state = planner.run(state)

print(updated_state)