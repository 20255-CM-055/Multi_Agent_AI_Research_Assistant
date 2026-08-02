from graph.builder.research_graph import research_graph

state = {
    "query": "Agentic AI",
    "research_plan": None,
    "retrieved_documents": None,
    "web_results": None,
    "final_report": None,
    "current_agent": None,
}

try:
    for event in research_graph.stream(
        state,
        stream_mode="updates",
    ):
        print(event)

    print("\n✅ Graph completed successfully!")

except Exception as e:
    print("\n❌ ERROR OCCURRED:")
    print(type(e).__name__)
    print(e)