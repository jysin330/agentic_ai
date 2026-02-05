from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
client = OpenAI(
    api_key= os.environ.get("GOOGLE_API_KEY"),
    base_url= "https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model= "gemini-3-flash-preview",
    n=1,
    messages=[
        {"role": "system", "content": "you are an helpful assistant"},
        {"role": "user", "content": "Who are you?"}
    ]
)

print(response.choices[0].message.content)