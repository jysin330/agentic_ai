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

import requests


def get_weather(city:str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    
    response = requests.get(url)
    if response.status_code == 200 :
        return f"The weather in {city} is {response.text}"
    
    return "Something went wrong"

available_tools = {
    "get_weather": get_weather
}

    

SYSTEM_PROMPT = """
    You are an expert AI Assistent in resolving user queries using chain of thought.
    You work on START , PLAN, and OUTPUT steps.
    You need to first PLAN whats need to be done. The PLAN can be multiple steps.
    One you think enough PLAN has been done, finally you will give an output.
    You can also call a tool if required from the list of available tools.
    for every tool call wait 
    Rules:
    - Strictly follow the given JSON output formate.
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (that can be multiple times) and finally (which is going to displayed to the user).
    
    Output JSON Format:
    {{"step": "START" | "PLAN" | "OUTPUT" | "Tool" | "OBSERVE" , "content": "string", "tool": "string", "input":"string"}}
    
    Available Tools:
    - get_weather(city: str): Takes city name as an input string and returns the weather info about the city.
    
    Example 1:
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
    
    Example 2:
    START : What is the weather of delhi?
    PLAN : {{"step" : "PLAN": "content": "Seems like user is interested in getting weather of delhi in india."}}
    PLAN : {{"step" : "PLAN": "content": "Let's see if we have any available tool from the list of avalilable tools."}}
    PLAN : {{"step" : "PLAN": "content": "Great , we have get_weather tool available for this query."}}
    PLAN : {{"step" : "PLAN": "content": "I need to call get_weather tool for delhi as input for city"}}
    PLAN : {{"step" : "TOOL": ,"tool": "get_weather", "input": "delhi"}}
    PLAN : {{"step" : "OBSERVE": ,"tool": "get_weather", "output": "The Temperature of delhi is cloudy with 20 C"}}
    PLAN : {{"step" : "PLAN": "content": "Great! I got the weather info about delhi."}}
    OUTPUT : {{"step" : "OUTPUT": "content": "The current weather in delhi is 20 C with some cloudy sky."}}

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
            model= "gpt-4o",
            response_format={"type": "json_object"},
            messages=message_history
        )
    except Exception as e:
        print("ERROR:", e)
        break
    raw_output = response.choices[0].message.content
   
    message_history.append({"role": "assistant", "content": raw_output})
    parsed_output = json.loads(raw_output)
    
  
    if parsed_output.get("step") == "TOOL":
        tool_to_call = parsed_output.get("tool")
        tool_input = parsed_output.get("input")
        print(f"TOOL {tool_to_call}  {tool_input}")
        tool_response = available_tools[tool_to_call](tool_input)
        print(f"tool response {tool_response}")
        message_history.append({"role": "developer", "content": json.dumps(
            {"step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response}
        )})
        continue
    
    if parsed_output.get("step") == "PLAN":
        print("PLAN", parsed_output.get("content") )
        continue
    if parsed_output.get("step") == "OUTPUT":
        print("OUTPUT", parsed_output.get("content") )
        break
        