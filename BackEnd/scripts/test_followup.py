from services.followup_service import FollowupService

service = FollowupService()

results = service.retrieve_context(
    session_id=21,
    question="What are the benefits of AI automation?"
)

for r in results:
    print("=" * 80)
    print("Distance:", r["distance"])
    print(r["document"])