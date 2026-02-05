# Zero Short Prompting
# Zero shot prompting: The model is given a direct question or task without prior examples.

from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    api_key= os.environ.get("GOOGLE_API_KEY"),
    base_url= "https://generativelanguage.googleapis.com/v1beta/"
)
SYSTEM_PROMPT = "You should only answer the coding related  questions. Do not answer anything else. Your name is Alexa. If user ask something else other than coding say sorry."
response = client.chat.completions.create(
    model= "gemini-2.5-flash",
    n=1,
    messages= [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey can you write a python code to translate the work hello to hindi?"}
    ]
)

print(response.choices[0].message.content)
