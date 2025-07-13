from openai import OpenAI
from config import settings
from utils.prompts import SYSTEM_PROMPT

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def call_ai_for_recommendation(user_input: str) -> dict:
    response = client.chat.completions.create(
    model=settings.AI_MODEL,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ],
    
    temperature=0.6
    )

    try:
        content = response.choices[0].message.content
        return eval(content)  # Make sure your AI response is a valid Python dict string
    except Exception as e:
        raise RuntimeError("AI output parsing failed") from e
