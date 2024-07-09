import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def ask_openai(question):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
        )
        answer = response.choices[0].message.content.strip()

        return answer
    except Exception as e:
        print(f"Error communicating with OpenAI: {e}")
        return "An error occurred while getting the answer from OpenAI."