from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import requests

client = OpenAI()

def get_weather(city:str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    
    response = requests.get(url)
    if response.status_code == 200 :
        return f"The weather in {city} is {response.text}"
    
    return "Something went wrong"
    
    
def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {"role": "user", "content": user_query}
        ]
    )
    print(f"bot: {response.choices[0].message.content}")
    
print(get_weather("goa"))