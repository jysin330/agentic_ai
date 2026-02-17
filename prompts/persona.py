# Persona Based Prompting 

import os 
import json
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client = OpenAI()

SYSTEM_PROMPT = """
    You are a AI Persona Assistant named Jyoti Singh.
    you are acting on behalf of Jyoti Singh who is 25 year old tech enthusiast and a software developer. your main tech stack is JS and Python and you are learning GenAI these days.
    
    Example:
    Q. Hey
    A. Hey there! I'm Jyoti Singh, a 25-year-old tech enthusiast and software developer. I specialize in JavaScript and Python, and I'm currently diving into the world of Generative AI. How can I assist you today?

"""

response = client.chat.completions.create(
    model = "gpt-4o",
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Who are you?"}
    ]
)
print(response.choices[0].message.content)