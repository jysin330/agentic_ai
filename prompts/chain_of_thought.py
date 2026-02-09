import os
from openai import OpenAI
import json
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key= os.environ.get("GOOGLE_API_KEY"),
    base_url= "https://generativelanguage.googleapis.com/v1beta/"
)
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
response = client.chat.completions.create(
    model= "gemini-2.5-flash",
    response_format= { "type": "json_object" },
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user" , "content":"Hey, write a code to add n numbers in js"},
        # Manually keep adding messages to history
        {"role": "assistant" , "content": json.dumps({ "step": "PLAN", "content": "The user wants a Javascript code snippet to add 'n' numbers. I should provide a function that takes an arbitrary number of arguments or an array and sums them up."})},
        {"role": "assistant" , "content": json.dumps({"step": "PLAN", "content": "I will define a JavaScript function using rest parameters to accept 'n' numbers."})}
    ]
)

print(response.choices[0].message.content)