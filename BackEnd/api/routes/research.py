from fastapi import APIRouter, Depends

from api.dependencies import get_research_service
from schemas.research import (
    ResearchRequest,
    ResearchResponse,
)
from services.research import ResearchService
from fastapi.responses import StreamingResponse
import json

from schemas.research import (
    HistoryItemResponse,
    ResearchDetailResponse,
)

from schemas.followup import (
    FollowupRequest,
    FollowupResponse,
)

from api.dependencies import get_followup_service
from services.followup_service import FollowupService

router = APIRouter()


@router.post(
    "/research",
    response_model=ResearchResponse,
    tags=["Research"],
)


async def research(
    request: ResearchRequest,
    service: ResearchService = Depends(get_research_service),
):
    return service.process_research(
        request.query
    )

@router.get(
    "/research/stream",
    tags=["Research"],
)
async def research_stream(
    query: str,
    service: ResearchService = Depends(get_research_service),
):

    # def event_generator():

    #     for event in service.stream_research(query):
    #         yield f"data: {json.dumps(event)}\n\n"
    
    def event_generator():
        print("🚀 Generator started")

        for event in service.stream_research(query):
            print("📤 Sending:", event)
            yield f"data: {json.dumps(event)}\n\n"

        print("✅ Generator finished")

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
    )
    
@router.get(
    "/history",
    response_model=list[HistoryItemResponse],
)
def get_history(
    service: ResearchService = Depends(
        get_research_service
    ),
):

    sessions = service.get_history()

    return [
        HistoryItemResponse(
            id=session.id,
            query=session.query,
            created_at=session.created_at,
        )
        for session in sessions
    ]
    

@router.get(
    "/history/{research_id}",
    response_model=ResearchDetailResponse,
)
def get_history_by_id(
    research_id: int,
    service: ResearchService = Depends(
        get_research_service
    ),
):

    session = service.get_history_by_id(
        research_id
    )

    # return ResearchDetailResponse(
    #     id=session.id,
    #     query=session.query,
    #     research_plan=json.loads(
    #         session.research_plan
    #     ),
    #     final_report=session.final_report,
    #     created_at=session.created_at,
    # )
    return ResearchDetailResponse(
    id=session.id,
    query=session.query,
    research_plan=json.loads(session.research_plan),
    final_report=session.final_report,
    created_at=session.created_at,
    used_sources=json.loads(session.used_sources),
)
    

@router.delete(
    "/history/{research_id}",
    tags=["Research"],
)
def delete_history(
    research_id: int,
    service: ResearchService = Depends(
        get_research_service,
    ),
):

    service.delete_research(
        research_id,
    )

    return {
        "status": "success",
        "message": "Research deleted successfully.",
    }
    
@router.post(
    "/research/followup",
    response_model=FollowupResponse,
    tags=["Research"],
)
async def followup(
    request: FollowupRequest,
    service: FollowupService = Depends(
        get_followup_service,
    ),
):

    answer = service.generate_followup_answer(
        session_id=request.session_id,
        question=request.question,
    )

    return FollowupResponse(
        answer=answer,
    )