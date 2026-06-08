from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file.")

client = OpenAI(api_key=api_key)


def innovation_bot(problem_statement: str) -> str:
    """Generate a practical product innovation plan from a user problem statement."""
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a senior product innovation advisor. "
                    "Be practical, concise, and execution-focused."
                ),
            },
            {
                "role": "user",
                "content": f"""
Help me design a launch-ready solution for this problem:

Problem: {problem_statement}

Return your response in this exact structure:
1. Problem Reframe (2-3 lines)
2. Target Users (primary + secondary)
3. Core Solution (clear one-paragraph summary)
4. MVP Features (5 bullets)
5. 14-Day Execution Plan (day ranges)
6. Risks and Mitigations (3 items)
7. Monetization Strategy (starter approach)
""",
            },
        ],
    )

    return response.choices[0].message.content or "No response generated."


if __name__ == "__main__":
    user_problem = input("Enter a real-world problem you want to solve: ")
    result = innovation_bot(user_problem)
    print("\n" + result)
