from domain.document import Document
from graph.state.research_state import ResearchState
from services.search_service import SearchService
from core.logging import setup_logger
from services.memory_service import MemoryService
from services.ranking_service import RankingService

logger = setup_logger(__name__)

class RetrieverAgent:
    """
    Retrieves relevant documents from the web.
    """

    # def __init__(self) -> None:
    #     self.search_service = SearchService()
        
    def __init__(self) -> None:
        self.search_service = SearchService()
        self.memory_service = MemoryService()
        self.ranking_service = RankingService()

    def run(
        self,
        state: ResearchState,
    ) -> ResearchState:

        # query = state["query"]

        # results = self.search_service.search(query)
        documents = []
        
        memory_documents = self.memory_service.search(
            state["query"]
        )

        logger.info(
            f"Retrieved {len(memory_documents)} documents from Knowledge Base."
        )

        documents.extend(memory_documents)

        research_plan = state["research_plan"] or []

        for topic in research_plan:

            results = self.search_service.search(topic)

            for item in results["results"]:

                document = Document(
                    title=item["title"],
                    url=item["url"],
                    content=item["content"],
                    source="Tavily",
                )

                documents.append(document)


    # ********************
        # documents = self._remove_duplicates(documents)

        # memory_count = sum(
        #     1 for doc in documents
        #     if doc.source == "Memory"
        # )

        # web_count = sum(
        #     1 for doc in documents
        #     if doc.source == "Tavily"
        # )

        # logger.info(
        #     f"Retriever collected "
        #     f"{memory_count} memory docs and "
        #     f"{web_count} web docs."
        # )

        # documents = documents[:15]
        # *********************
        documents = self._remove_duplicates(documents)

        documents = self.ranking_service.rank(
            query=state["query"],
            documents=documents,
        )

        memory_count = sum(
            1 for doc in documents
            if doc.source == "Memory"
        )

        web_count = sum(
            1 for doc in documents
            if doc.source == "Tavily"
        )

        logger.info(
            f"Retriever collected "
            f"{memory_count} memory docs and "
            f"{web_count} web docs."
        )

        documents = documents[:15]

        state["retrieved_documents"] = documents
        state["current_agent"] = "Retriever"

        return state
    
    
    def _remove_duplicates(
        self,
        documents: list[Document],
    ) -> list[Document]:

        seen = set()
        unique_documents = []

        for document in documents:

            key = (
                document.title.strip().lower(),
                # hash(document.content.strip()),
                document.content.strip(),
            )

            if key in seen:
                continue

            seen.add(key)
            unique_documents.append(document)

        logger.info(
            f"Removed {len(documents) - len(unique_documents)} duplicate documents."
        )

        return unique_documents
        
