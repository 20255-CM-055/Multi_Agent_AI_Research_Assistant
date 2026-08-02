from graph.state.research_state import ResearchState
from agents.evaluator.constants import (
    BLOCKED_PHRASES,
    MIN_CONTENT_LENGTH,
)

class EvaluatorAgent:
    """
    Filters low-quality retrieved documents.
    """

    MIN_CONTENT_LENGTH = 200

    BLOCKED_PHRASES = [
        "share on facebook",
        "share on linkedin",
        "cookie",
        "privacy policy",
        "terms of service",
        "skip to main content",
        "advertisement",
    ]

    def run(
        self,
        state: ResearchState,
    ) -> ResearchState:

        documents = state["retrieved_documents"] or []

        filtered_documents = []

        for document in documents:

            content = document.content.lower()

            if len(content) < self.MIN_CONTENT_LENGTH:
                continue

            if any(
                phrase in content
                for phrase in self.BLOCKED_PHRASES
            ):
                continue

            filtered_documents.append(document)

        state["retrieved_documents"] = filtered_documents
        state["current_agent"] = "Evaluator"

        return state