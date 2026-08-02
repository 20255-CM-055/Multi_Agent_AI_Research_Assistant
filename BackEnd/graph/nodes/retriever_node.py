from agents.retriever.retriever import RetrieverAgent
from graph.state.research_state import ResearchState

retriever = RetrieverAgent()


def retriever_node(
    state: ResearchState,
) -> ResearchState:

    return retriever.run(state)