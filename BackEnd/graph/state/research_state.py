from typing import List, Optional

from typing_extensions import TypedDict
from domain.document import Document

class ResearchState(TypedDict):
    """
    Shared state used by the Research Workflow.

    Every LangGraph node receives this state,
    updates it, and returns it.
    """

    # User Input
    query: str

    # Planner
    research_plan: Optional[List[str]]

    # Retriever
    retrieved_documents: Optional[List[Document]]

    # Web Search
    web_results: Optional[List[str]]

    # Writer
    final_report: Optional[str]
    
    # Sources used in the final report
    used_sources: Optional[List[dict]]

    # Workflow
    current_agent: Optional[str]    