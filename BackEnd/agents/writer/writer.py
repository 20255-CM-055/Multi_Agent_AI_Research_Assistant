from agents.writer.prompt import WRITER_PROMPT
from graph.state.research_state import ResearchState
from services.llm_service import LLMService
from core.logging import setup_logger
from knowledge_base.ingest import ingest_document

logger = setup_logger(__name__)

class WriterAgent:
    """
    Generates the final research report.
    """

    def __init__(self) -> None:
        self.llm = LLMService()
# ***********
    # def _format_documents(self, state: ResearchState) -> str:
    #     """
    #     Converts retrieved documents into
    #     a prompt-friendly format.
    #     """

    #     return "\n\n".join(
    #         f"""
    #     ========================
    #     Document [{index}]
    #     ========================

    #     Title:
    #     {doc.title}

    #     Source:
    #     {doc.source}

    #     URL:
    #     {doc.url}

    #     Content:
    #     {doc.content}
    #     """
    #         for index, doc in enumerate(
    #             state["retrieved_documents"] or [],
    #             start=1,
    #         )
    #     )
    #         for doc in state["retrieved_documents"] or []
    #     )
    def _format_documents(self, state: ResearchState) -> str:
        """
        Converts retrieved documents into
        a prompt-friendly format.
        """

        return "\n\n".join(
            f"""
    ========================
    Document [{index}]
    ========================

    Title:
    {doc.title}

    Source:
    {doc.source}

    URL:
    {doc.url}

    Content:
    {doc.content}
    """
            for index, doc in enumerate(
                state["retrieved_documents"] or [],
                start=1,
            )
        )

# **************
    def _build_prompt(self, state: ResearchState) -> str:
        """
        Creates the final prompt.
        """

        return WRITER_PROMPT.format(
            query=state["query"],
            documents=self._format_documents(state),
        )

    def _append_references(self, report: str, state: ResearchState) -> str:
        """
        Appends references to the report.
        """

        report += "\n\n---\n\n## References\n\n"

        for index, document in enumerate(
            state["retrieved_documents"] or [],
            start=1,
        ):

            report += (
                f"[{index}] {document.title}\n"
                f"{document.url}\n\n"
            )

        return report

    def run(
        self,
        state: ResearchState,
    ) -> ResearchState:

        prompt = self._build_prompt(state)

        report = self.llm.generate(prompt)

        report = self._append_references(
            report,
            state,
        )
        # print("========== Saving Report ==========")
        logger.info("Saving report to Knowledge Base...")
        try:
            ingest_document(
                text=report,
                metadata={
                    "topic": state["query"],
                    "source": "generated_report",
                },
            )
            # print("========== Report Saved ==========")
            # logger.info("Report saved to Knowledge Base.")
            logger.info("Report saved to Knowledge Base.")

        except Exception as e:
            logger.error(
                f"Failed to save report to Knowledge Base: {e}"
            )
        
        
        

        # state["final_report"] = report
        # state["current_agent"] = "Writer"
        state["final_report"] = report

        state["used_sources"] = [
            {
                "title": doc.title,
                "url": doc.url,
                "source": doc.source,
            }
            for doc in state["retrieved_documents"] or []
        ]

        state["current_agent"] = "Writer"

        return state