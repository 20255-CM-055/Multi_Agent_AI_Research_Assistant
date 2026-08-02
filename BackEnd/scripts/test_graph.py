from graph.builder.research_graph import research_graph

state = {
    "query": "Agentic AI",
    "research_plan": None,
    "retrieved_documents": None,
    "web_results": None,
    "final_report": None,
    "current_agent": None,
}

result = research_graph.invoke(state)

print(result)