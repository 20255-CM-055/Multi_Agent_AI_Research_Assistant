from agents.writer.writer import WriterAgent
from graph.state.research_state import ResearchState

writer = WriterAgent()


def writer_node(
    state: ResearchState,
) -> ResearchState:
    """
    Executes the Writer Agent.
    """

    return writer.run(state)