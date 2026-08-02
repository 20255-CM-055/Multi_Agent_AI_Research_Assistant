from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.health import router as health_router
from config.settings import settings
from core.lifespan import lifespan
from api.v1.router import api_router

from core.exception_handlers import (
    database_exception_handler,
    research_exception_handler,
)

from core.exceptions import (
    DatabaseError,
    ResearchGenerationError,
)

from core.middleware import logging_middleware


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Production-grade AI Research Assistant built with LangGraph",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(health_router)
app.include_router(api_router)

app.add_exception_handler(
    ResearchGenerationError,
    research_exception_handler,
)

app.add_exception_handler(
    DatabaseError,
    database_exception_handler,
)

app.middleware("http")(logging_middleware)