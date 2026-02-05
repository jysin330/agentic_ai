# Few Shot prompting 
# Few Shot Prompting : Directly giving the instruction to the model and few examples to the model. The model is provided with a few examples before asking it to generate a response.

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
client = OpenAI(
    api_key= os.environ.get("GOOGLE_API_KEY"),
    base_url= "https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
    you should only and only answer the coding related questions. Do not  answer anythin else. Your name is Alexa . If user asks something otehr than coding , just say sorry.
    
    Examples:
    Q: Can you explain the a +b whole square?
    A: Sorry, i can only help with coding related questions.
    
    Q: Hey , Write a code in python for adding two numbers.
    A: def(a, b):
          return a+b
"""

response = client.chat.completions.create(
    model= "gemini-2.5-flash",
    n=1,
    messages= [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, Can you explain a+b whole squre."}
    ]
)

print(response.choices[0].message.content)