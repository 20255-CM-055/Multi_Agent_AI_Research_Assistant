import json

from sqlalchemy.orm import Session

from database.models import ResearchSession
from core.exceptions import DatabaseError

from domain.document import Document

from dataclasses import asdict

class ResearchRepository:
    """
    Handles all database operations for research sessions.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:
        print("Repository file:", __file__) 
        self.db = db

    def save(
    self,
    query: str,
    research_plan: list[str],
    final_report: str,
    retrieved_documents: list[Document],
    used_sources: list[dict],
) -> ResearchSession:
        print(">>> SAVE FUNCTION HIT <<<")  
        
        print(locals().keys())   
        

        session = ResearchSession(
            query=query,
            research_plan=json.dumps(research_plan),
            final_report=final_report,
            # retrieved_documents=json.dumps([doc.dict() for doc in retrieved_documents]),
            retrieved_documents=json.dumps([asdict(doc) for doc in retrieved_documents]),
            used_sources=json.dumps(used_sources),
        )

        try:

            self.db.add(session)

            self.db.commit()

            self.db.refresh(session)

            return session   # 👈 THIS IS MISSING

        except Exception as e:

            self.db.rollback()

            raise DatabaseError(
                "Failed to save research session."
            ) from e
    
    # 👇 ADD IT HERE
    def get_by_id(
        self,
        research_id: int,
    ) -> ResearchSession:

        try:

            session = (
                self.db.query(ResearchSession)
                .filter(
                    ResearchSession.id == research_id
                )
                .first()
            )

            if session is None:
                raise DatabaseError(
                    "Research session not found."
                )

            return session

        except DatabaseError:
            raise

        except Exception as e:
            raise DatabaseError(
                "Failed to fetch research session."
            ) from e
    
    def get_all(self) -> list[ResearchSession]:

        try:
            sessions = (
                self.db.query(ResearchSession)
                .order_by(ResearchSession.created_at.desc())
                .all()
            )

            return sessions

        except Exception as e:
            raise DatabaseError(
                "Failed to fetch research history."
            ) from e
            
    def delete(
    self,
    research_id: int,
) -> None:

        try:

            session = (
                self.db.query(ResearchSession)
                .filter(
                    ResearchSession.id == research_id
                )
                .first()
            )

            if session is None:
                raise DatabaseError(
                    "Research session not found."
                )

            self.db.delete(session)

            self.db.commit()

        except DatabaseError:
            raise

        except Exception as e:

            self.db.rollback()

            raise DatabaseError(
                "Failed to delete research session."
            ) from e