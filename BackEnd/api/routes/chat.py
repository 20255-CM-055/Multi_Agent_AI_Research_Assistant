from fastapi import APIRouter, Depends, HTTPException

from api.dependencies import (
    get_conversation_service,
    get_llm_service,
    get_research_repository,
)

from repositories.research_repository import ResearchRepository
# from services import memory_service
from services.conversation_service import ConversationService
from services.llm_service import LLMService

from schemas.chat import ChatRequest, ChatResponse

from api.dependencies import (
    get_memory_service,
)

from services.memory_service import MemoryService

router = APIRouter()


@router.post(
    "/chat/{research_id}",
    response_model=ChatResponse,
)

# def chat(
#     research_id: int,
#     request: ChatRequest,
#     research_repository: ResearchRepository = Depends(
#         get_research_repository,
#     ),
#     conversation_service: ConversationService = Depends(
#         get_conversation_service,
#     ),
#     llm_service: LLMService = Depends(
#         get_llm_service,
#     ),
# ):
def chat(
    research_id: int,
    request: ChatRequest,
    research_repository: ResearchRepository = Depends(
        get_research_repository,
    ),
    conversation_service: ConversationService = Depends(
        get_conversation_service,
    ),
    llm_service: LLMService = Depends(
        get_llm_service,
    ),
    memory_service: MemoryService = Depends(
        get_memory_service,
    ),
):
    try:
        print(f"Research ID received: {research_id}")
        research = research_repository.get_by_id(
            research_id,
        )
        print(research.final_report)
        history = conversation_service.get_history(
    research_id,
)
        memory_docs = memory_service.search(
    query=request.message,
    top_k=5,
)
        print("\n========== MEMORY DOCS ==========")
        print(f"Retrieved {len(memory_docs)} documents")

        for i, doc in enumerate(memory_docs, 1):
            print(f"\n--- Document {i} ---")
            print(doc.content[:300])   # first 300 chars

        print("=================================\n")

        context = "\n\n".join(
            doc.content
            for doc in memory_docs
        )
        conversation_text = ""

        for message in history:
            # conversation_text += (
            #     f"{message.role}: {message.content}\n"
            # )
            conversation_text += (
    f"{message.role}: {message.message}\n"
)

#         prompt = f"""
# You are an AI Research Assistant.

# Original Research Query:
# {research.query}

# # Research Report:
# # {research.final_report}

# Relevant Research Context:

# {context}

# Conversation History:
# {conversation_text}

# Current User Question:
# {request.message}

# Instructions:
# - Answer ONLY using the research report and conversation history.
# - If the answer is not available, clearly say you don't have enough information.
# - Keep the conversation natural.
# - Do not invent facts.
# """

            prompt = f"""
You are an expert AI Research Assistant.

Original Research Topic:
{research.query}

Complete Research Report:
{research.final_report}

Relevant Retrieved Context:
{context}

Conversation History:
{conversation_text}

Current User Question:
{request.message}

Instructions:

- Use the COMPLETE RESEARCH REPORT as your primary source.
- Use the retrieved context only to support your answer.
- Use conversation history only to maintain context.
- Never say "According to the conversation history..."
- Answer naturally.
- If the report does not contain the answer, say so.
"""

        answer = llm_service.generate(
            prompt,
        )

        conversation_service.save_user_message(
            research_id,
            request.message,
        )

        conversation_service.save_assistant_message(
            research_id,
            answer,
        )

        return ChatResponse(
            answer=answer,
        )

    # except Exception:

    #     raise HTTPException(
    #         status_code=404,
    #         detail="Research session not found.",
    #     )
    except Exception as e:
        print("ERROR:", e)
        raise