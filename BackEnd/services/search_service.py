from tavily import TavilyClient

from core.config import settings


class SearchService:
    """
    Handles web search using Tavily.
    """

    def __init__(self) -> None:
        self.client = TavilyClient(
            api_key=settings.TAVILY_API_KEY
        )

    def search(
        self,
        query: str,
        max_results: int = 5,
    ):

        return self.client.search(
            query=query,
            max_results=max_results,
        )