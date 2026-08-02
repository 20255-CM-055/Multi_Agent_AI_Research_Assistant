from agents.evaluator.evaluator import EvaluatorAgent
from graph.state.research_state import ResearchState

evaluator = EvaluatorAgent()


def evaluator_node(
    state: ResearchState,
) -> ResearchState:
    """
    Executes the Evaluator Agent.
    """

    return evaluator.run(state)