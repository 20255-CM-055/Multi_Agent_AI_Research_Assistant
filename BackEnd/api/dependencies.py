




from fastapi import Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from services.llm_service import LLMService

from repositories.research_repository import ResearchRepository
from repositories.conversation_repository import ConversationRepository

from services.research import ResearchService
from services.conversation_service import ConversationService

# from services.llm_service import LLMService

from services.memory_service import MemoryService
from services.followup_service import FollowupService

def get_research_repository(
    db: Session = Depends(get_db),
) -> ResearchRepository:

    return ResearchRepository(db)


def get_conversation_repository(
    db: Session = Depends(get_db),
) -> ConversationRepository:

    return ConversationRepository(db)


def get_conversation_service(
    repository: ConversationRepository = Depends(
        get_conversation_repository
    ),
) -> ConversationService:

    return ConversationService(repository)


# def get_research_service(
#     repository: ResearchRepository = Depends(
#         get_research_repository
#     ),
#     conversation_service: ConversationService = Depends(
#         get_conversation_service
#     ),
# ) -> ResearchService:

#     return ResearchService(
#         repository,
#         conversation_service,
#     )

def get_llm_service() -> LLMService:
    return LLMService()

def get_followup_service(
    llm_service: LLMService = Depends(
        get_llm_service,
    ),
) -> FollowupService:

    return FollowupService(
        llm_service,
    )

def get_research_service(
    repository: ResearchRepository = Depends(
        get_research_repository
    ),
    conversation_service: ConversationService = Depends(
        get_conversation_service
    ),
    llm_service: LLMService = Depends(
        get_llm_service
    ),
) -> ResearchService:

        return ResearchService(
            repository,
            conversation_service,
            llm_service,
        )
    

def get_memory_service():
    return MemoryService()
# def get_llm_service() -> LLMService:
#     return LLMService()