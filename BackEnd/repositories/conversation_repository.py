from sqlalchemy.orm import Session

from database.models import ConversationMessage
from core.exceptions import DatabaseError


class ConversationRepository:

    def __init__(self, db: Session):
        self.db = db

    def save_message(
        self,
        research_session_id: int,
        role: str,
        message: str,
    ) -> ConversationMessage:

        conversation = ConversationMessage(
            research_session_id=research_session_id,
            role=role,
            message=message,
        )

        try:
            self.db.add(conversation)
            self.db.commit()
            self.db.refresh(conversation)

            return conversation

        except Exception as e:
            self.db.rollback()

            raise DatabaseError(
                "Failed to save conversation."
            ) from e

    def get_messages(
        self,
        research_session_id: int,
    ) -> list[ConversationMessage]:

        try:
            return (
                self.db.query(ConversationMessage)
                .filter(
                    ConversationMessage.research_session_id
                    == research_session_id
                )
                .order_by(
                    ConversationMessage.created_at
                )
                .all()
            )

        except Exception as e:
            raise DatabaseError(
                "Failed to fetch conversation."
            ) from e