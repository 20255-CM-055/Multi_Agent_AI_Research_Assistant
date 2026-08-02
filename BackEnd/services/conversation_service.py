from repositories.conversation_repository import ConversationRepository


class ConversationService:

    def __init__(
        self,
        conversation_repository: ConversationRepository,
    ):
        self.repository = conversation_repository

    def save_user_message(
        self,
        research_session_id: int,
        message: str,
    ):

        return self.repository.save_message(
            research_session_id,
            "user",
            message,
        )

    def save_assistant_message(
        self,
        research_session_id: int,
        message: str,
    ):

        return self.repository.save_message(
            research_session_id,
            "assistant",
            message,
        )

    def get_history(
        self,
        research_session_id: int,
    ):

        return self.repository.get_messages(
            research_session_id
        )