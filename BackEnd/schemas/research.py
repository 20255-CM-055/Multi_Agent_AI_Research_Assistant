from typing import List, Optional

from pydantic import BaseModel

from datetime import datetime


class ResearchRequest(BaseModel):
    query: str


    
# class ResearchResponse(BaseModel):
#     id: int | None = None

#     status: str

#     query: str

#     current_agent: Optional[str] = None

#     research_plan: Optional[List[str]] = None

#     used_sources: list[dict] | None = None

#     final_report: Optional[str] = None

class ResearchResponse(BaseModel):
    id: int | None = None

    status: str

    query: str

    current_agent: Optional[str] = None

    research_plan: Optional[List[str]] = None

    used_sources: list[dict] | None = None

    final_report: Optional[str] = None

    suggested_questions: list[str] = []
    
class HistoryItemResponse(BaseModel):
    id: int
    query: str
    created_at: datetime
    

# class ResearchDetailResponse(BaseModel):
#     id: int
#     query: str
#     research_plan: list[str]
#     final_report: str
#     created_at: datetime

class ResearchDetailResponse(BaseModel):
    id: int
    query: str
    research_plan: list[str]
    final_report: str
    created_at: datetime

    used_sources: list[dict] = []