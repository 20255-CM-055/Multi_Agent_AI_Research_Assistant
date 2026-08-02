from contextlib import asynccontextmanager

from fastapi import FastAPI

from config.logging import logger
from database.database import Base, engine
from database.models import ResearchSession


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles application startup and shutdown events.
    """

    logger.info("Application startup...")

    # Create database tables
    Base.metadata.create_all(bind=engine)

    yield

    logger.info("Application shutdown...")