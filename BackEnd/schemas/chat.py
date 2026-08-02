from pydantic import BaseModel

from api.dependencies import (
    get_memory_service,
)

from services.memory_service import MemoryService

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str