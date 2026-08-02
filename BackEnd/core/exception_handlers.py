from fastapi import Request
from fastapi.responses import JSONResponse

from core.exceptions import (
    DatabaseError,
    ResearchGenerationError,
)
from core.logging import setup_logger

logger = setup_logger(__name__)


async def research_exception_handler(
    request: Request,
    exc: ResearchGenerationError,
):
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": str(exc),
        },
    )


async def database_exception_handler(
    request: Request,
    exc: DatabaseError,
):
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": str(exc),
        },
    )