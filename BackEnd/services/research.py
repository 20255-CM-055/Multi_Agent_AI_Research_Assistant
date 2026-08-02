from unittest import result

from graph.builder.research_graph import research_graph
from repositories.research_repository import ResearchRepository
from schemas.research import ResearchResponse
from core.exceptions import ResearchGenerationError
from services.conversation_service import ConversationService
from services.llm_service import LLMService
from services.report_vector_service import ReportVectorService

class ResearchService:

#     def __init__(
#     self,
#     repository: ResearchRepository,
#     conversation_service: ConversationService,
# ):
    def __init__(
        self,
        repository: ResearchRepository,
        conversation_service: ConversationService,
        llm_service: LLMService,
        # report_vector_service: ReportVectorService,
    ):
        # self.repository = repository
        # self.conversation_service = conversation_service
        self.llm_service = llm_service
        self.repository = repository
        self.conversation_service = conversation_service
        self.report_vector_service = ReportVectorService()

    def process_research(
        self,
        query: str,
    ) -> ResearchResponse:

    
        initial_state = {
    "query": query,
    "research_plan": None,
    "retrieved_documents": None,
    "web_results": None,
    "final_report": None,
    "used_sources": None,
    "current_agent": None,
}

        # result = research_graph.invoke(initial_state)
        try:

            result = research_graph.invoke(initial_state)

        # except Exception as e:
        #     raise ResearchGenerationError(
        #         "Failed to generate research report."
        #     ) from e
        except Exception as e:
            import traceback

            print("\n" + "=" * 80)
            print("ACTUAL ERROR")
            print("=" * 80)
            traceback.print_exc()
            print("=" * 80 + "\n")

            raise
        
        print("STEP 1: Saving session...")
        session = self.repository.save(
            query=result["query"],
            research_plan=result["research_plan"],
            final_report=result["final_report"],
            retrieved_documents=result["retrieved_documents"],
            used_sources=result["used_sources"],
        )
        print("STEP 2: Indexing report...")
        self.report_vector_service.index_report(
    session_id=session.id,
    report=result["final_report"],
)
        print("STEP 3: Saving conversation...")
        self.conversation_service.save_user_message(
    session.id,
    result["query"],
)

        self.conversation_service.save_assistant_message(
            session.id,
            result["final_report"],
        )
        print("STEP 4: Generating followup questions...")
        questions = self.llm_service.generate_followup_questions(
    result["final_report"],
)
        print("STEP 4 DONE")


        return ResearchResponse(
status="success",
    query=result["query"],
    current_agent=result["current_agent"],
    research_plan=result["research_plan"],
    final_report=result["final_report"],
    used_sources=result["used_sources"],
    suggested_questions=questions,
)
    

    def stream_research(
    self,
    query: str,
):
        initial_state = {
            "query": query,
            "research_plan": None,
            "retrieved_documents": None,
            "web_results": None,
            "final_report": None,
            "used_sources": None,
            "current_agent": None,
        }

        try:

            final_result = None

            for event in research_graph.stream(
                initial_state,
                stream_mode="updates",
            ):
                node_name = next(iter(event))
                final_result = event[node_name]
                print("\n======================")
                print("NODE:", node_name)
                print("CURRENT_AGENT:", final_result.get("current_agent"))
                print("STATE KEYS:", list(final_result.keys()))
                print("======================\n")
                print("\n============================")
                print("NODE:", node_name)
                print("CURRENT AGENT:", final_result.get("current_agent"))
                print("EVENT:", event)
                print("============================")

                
                yield {
    "type": "progress",
    "agent": node_name,
    "current_agent": final_result["current_agent"],
}

            print("STEP 1: Saving session...")
            session = self.repository.save(
    query=final_result["query"],
    research_plan=final_result["research_plan"],
    final_report=final_result["final_report"],
    retrieved_documents=final_result["retrieved_documents"],
    used_sources=final_result["used_sources"],
)
            print("STEP 2: Indexing report...")
            self.report_vector_service.index_report(
    session_id=session.id,
    report=final_result["final_report"],
)
            print("STEP 3: Saving conversation...")
            self.conversation_service.save_user_message(
                session.id,
                final_result["query"],
            )

            self.conversation_service.save_assistant_message(
                session.id,
                final_result["final_report"],
            )
            print("STEP 4: Generating followup questions...")
            questions = self.llm_service.generate_followup_questions(
    final_result["final_report"],
)
            print("STEP 4 DONE")
            print("===== SENDING COMPLETED EVENT =====")
            print(final_result["final_report"][:200])

           

            print("STEP 5: Sending completed event...")
            yield {
  "type": "completed",
    "id": session.id,
    "status": "success",
    "query": final_result["query"],
    "research_plan": final_result["research_plan"],
    "final_report": final_result["final_report"],
    "used_sources": final_result["used_sources"],
    "suggested_questions": questions,
}

        # except Exception as e:
        #     raise ResearchGenerationError(
        #         "Failed to generate research report."
        #     ) from e
        except Exception:
            import traceback

            print("\n" + "=" * 80)
            print("STREAM ERROR")
            print("=" * 80)

            traceback.print_exc()

            print("=" * 80)

            raise
        
    def get_history(self):
        """
        Returns all research sessions.
        """

        return self.repository.get_all()
    
    def get_history_by_id(
        self,
        research_id: int,
    ):
        """
        Returns a single research session.
        """

        return self.repository.get_by_id(research_id)
    
    def delete_research(
    self,
    research_id: int,
):
        """
        Deletes a research session.
        """

        self.repository.delete(
            research_id
        )