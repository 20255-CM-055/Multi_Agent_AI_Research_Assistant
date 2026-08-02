import json

from database.database import SessionLocal
from repositories.research_repository import ResearchRepository


db = SessionLocal()

repository = ResearchRepository(db)

sessions = repository.get_all()

for session in sessions:

    print("=" * 50)
    print("ID:", session.id)
    print("Query:", session.query)
    print("Research Plan:", json.loads(session.research_plan))
    print("Created At:", session.created_at)

db.close()