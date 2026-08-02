from pydantic import BaseModel


class FollowupRequest(BaseModel):
    session_id: int
    question: str


class FollowupResponse(BaseModel):
    answer: str