from fastapi import APIRouter
from api.routes.health import router as health_router
from api.routes.research import router as research_router
from api.routes.chat import router as chat_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    health_router,
    tags=["Health"],
)

api_router.include_router(
    research_router,
    tags=["Research"],
)

api_router.include_router(
    chat_router,
    tags=["Chat"],
)