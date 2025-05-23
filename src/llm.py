from openai import OpenAI
from src.prompt import system_instruction

client = OpenAI()

messages = [
    {"role": "system", "content": system_instruction}
]

def ask_order(messages, model = "gpt-4o-mini", temperature = 0):
    reponse = client.chat.completions.create(
        model = model,
        messages= messages,
        temperature=temperature
    )

    return reponse.choices[0].message.content