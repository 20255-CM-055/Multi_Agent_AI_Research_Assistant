from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import DateTime
# from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    DateTime,
    ForeignKey,
)


from database.database import Base




class ResearchSession(Base):

    __tablename__ = "research_sessions"

    id = Column(Integer, primary_key=True, index=True)

    query = Column(Text)

    research_plan = Column(Text)

    final_report = Column(Text)

    # NEW
    retrieved_documents = Column(Text)

    # NEW
    used_sources = Column(Text)
    
    messages = relationship(
        "ConversationMessage",
        back_populates="research_session",
        cascade="all, delete-orphan",
    )

    created_at = Column(
        DateTime,
        # default=datetime.utcnow,
        default=datetime.now,
    )
    

class ConversationMessage(Base):
    __tablename__ = "conversation_messages"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    research_session_id = Column(
        Integer,
        ForeignKey("research_sessions.id"),
        nullable=False,
    )

    role = Column(
        String,
        nullable=False,
    )

    message = Column(
        Text,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        # default=datetime.utcnow,
        default=datetime.now,
    )

    research_session = relationship(
        "ResearchSession",
        back_populates="messages",
    )