from agents.planner.planner import PlannerAgent
from graph.state.research_state import ResearchState

planner = PlannerAgent()


def planner_node(state: ResearchState) -> ResearchState:
    """
    Executes the Planner Agent.
    """

    return planner.run(state)