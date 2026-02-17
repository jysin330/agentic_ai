import os
from openai import OpenAI
import json
from dotenv import load_dotenv
load_dotenv()
import re

# client = OpenAI(
#     api_key= os.environ.get("GOOGLE_API_KEY"),
#     base_url= "https://generativelanguage.googleapis.com/v1beta/"
# )
client = OpenAI()
print(os.environ.get("GOOGLE_API_KEY"))

SYSTEM_PROMPT = """
    You are an expert AI Assistent in resolving user queries using chain of thought.
    You work on START , PLAN, and OUTPUT steps.
    You need to first PLAN whats need to be done. The PLAN can be multiple steps.
    One you think enough PLAN has been done, finally you will give an output.
    Rules:
    - Strictly follow the given JSON output formate.
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (that can be multiple times) and finally (which is going to displayed to the user).
    
    Output JSON Format:
    {{"step": "START" | "PLAN" | "OUTPUT", "content": "string"}}
    
    Example:
    START : Hey , Can you solve 2 + 3 * 5 / 10
    PLAN : {{"step" : "PLAN": "content": "Seems like user is interested in math problem"}}
    PLAN : {{"step" : "PLAN": "content": "Looking at the problem , we should solve this using BODMAS method"}}
    PLAN : {{"step" : "PLAN": "content": "Yes, the BODMAS is correct thing to be done here"}}
    PLAN : {{"step" : "PLAN": "content": "First we must multipy 3*5 which is 15"}}
    PLAN : {{"step" : "PLAN": "content": "Now the new equation is 2 + 15 / 10"}}
    PLAN : {{"step" : "PLAN": "content": "We must perform divide that is 15 / 10 = 1.5"}}
    PLAN : {{"step" : "PLAN": "content": "Now the new equation is 2 + 1.5"}}
    PLAN : {{"step" : "PLAN": "content": "Finally lets perform the add, its gives 3.5 "}}
    PLAN : {{"step" : "PLAN": "content": "Great , we have solved and finally left with 3.5 as answer "}}
    OUTPUT : {{"step" : "OUTPUT": "content": "3.5"}}

"""


message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
    
]
user_query = input("")
message_history.append({"role": "user", "content": user_query})
out = True
while True:
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=message_history
        )
    except Exception:
        import time
        print("Rate limit hit, waiting...")
        time.sleep(50)
        continue
    raw_output = response.choices[0].message.content
   
    message_history.append({"role": "assistant", "content": json.dumps(raw_output)})
    parsed_output = json.loads(raw_output)
    if parsed_output.get("step") == "START":
        print("START", parsed_output.get("content") )
        continue
    
    if parsed_output.get("step") == "PLAN":
        print("PLAN", parsed_output.get("content") )
        continue
    if parsed_output.get("step") == "OUTPUT":
        print("OUTPUT", parsed_output.get("content") )
        break
        