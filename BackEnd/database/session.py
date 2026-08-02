from database.database import engine
from database.database import Base

from database.models import ResearchSession

def create_database():

    Base.metadata.create_all(
        bind=engine
    )