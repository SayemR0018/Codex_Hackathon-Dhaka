from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#mentor bot 
def mentor_bot(user_idea):
    response = client.chat.completions.create(
        model="gpt-5.5", #make changes to the model

    #give it a role and prompt/content
        messages=[{
            "role": "user",
            "content": f"""
        You are a hackathon mentor.
        Help the user turn this idea into a hackathon project:

        Idea: {user_idea}

        Return:
        1. Improved idea
        2. MVP features
        3. Tech stack
        4. API usage
        5. 24-hour build plan
        6. Pitch advice
        """
        }]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    user_idea = input("Enter your hackathon idea: ")
    result = mentor_bot(user_idea)
    print("\n" + result)
