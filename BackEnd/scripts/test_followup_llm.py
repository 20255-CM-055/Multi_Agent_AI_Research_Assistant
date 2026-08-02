from services.followup_service import FollowupService
from services.llm_service import LLMService

followup_service = FollowupService()
llm_service = LLMService()

answer = followup_service.generate_followup_answer(
    session_id=21,
    question="What are the benefits of AI automation?",
    llm_service=llm_service,
)

print(answer)