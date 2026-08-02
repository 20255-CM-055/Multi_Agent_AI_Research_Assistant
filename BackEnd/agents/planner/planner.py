from graph.state.research_state import ResearchState
from services.llm_service import LLMService
from agents.planner.prompt import PLANNER_PROMPT
from core.logging import setup_logger

logger = setup_logger(__name__)

class PlannerAgent:
    """
    Generates a research plan using an LLM.
    """

    def __init__(self) -> None:
        self.llm = LLMService()

    def run(self, state: ResearchState) -> ResearchState:

        query = state["query"]

        prompt = PLANNER_PROMPT.format(
            query=query
        )

        response = self.llm.generate(prompt)

        research_plan = [
            line.strip()
            for line in response.splitlines()
            if line.strip()
        ]

        state["research_plan"] = research_plan
        state["current_agent"] = "Planner"

        return state
    
    