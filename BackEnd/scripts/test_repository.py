from database.database import SessionLocal
from repositories.research_repository import ResearchRepository


db = SessionLocal()

repository = ResearchRepository(db)

session = repository.save(
    query="Agentic AI",
    research_plan=[
        "Introduction",
        "Applications",
    ],
    final_report="This is a test report.",
)

print(session.id)

db.close()