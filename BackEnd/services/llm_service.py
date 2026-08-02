from groq import Groq

from core.config import settings


class LLMService:
    """
    Handles all interactions with the Groq API.
    """

    def __init__(self) -> None:
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate(
        self,
        prompt: str,
        model: str = "llama-3.3-70b-versatile",
    ) -> str:
        """
        Generate a response using Groq.
        """

        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content
    
    def generate_followup_questions(
    self,
    report: str,
    model: str = "llama-3.3-70b-versatile",
) -> list[str]:
        """
        Generate suggested follow-up questions for a research report.
        """

        prompt = f"""
    You are helping users continue a research conversation.

    Based ONLY on the research report below, generate exactly 4 follow-up questions.

    Rules:
    - Questions must be directly related to the report.
    - Keep each question under 10 words.
    - Do not number the questions.
    - Do not use bullet points.
    - Return one question per line.
    - Do not include any explanation.

    Research Report:

    {report}
    """

        response = self.generate(
            prompt=prompt,
            model=model,
        )

        questions = [
            line.strip("-• ").strip()
            for line in response.splitlines()
            if line.strip()
        ]

        return questions[:4]


    def generate_followup_answer(
        self,
        session_id: int,
        question: str,
        llm_service,
    ):
        chunks = self.retrieve_context(
            session_id=session_id,
            question=question,
        )

        context = "\n\n".join(
            chunk["document"]
            for chunk in chunks
        )

        prompt = f"""
    You are an AI Research Assistant.

    Answer the user's question ONLY using the research report context below.

    Rules:
    - If the answer exists in the report context, answer from the report.
    - Do not invent information.
    - If the report does not contain the answer:
        - First say:
        "This information is not covered in the research report."
        - Then answer using your general knowledge.
        - Clearly mention that the remaining answer is based on general knowledge.

    Research Report Context:
    {context}

    User Question:
    {question}
    """

        answer = llm_service.generate(prompt)

        return answer