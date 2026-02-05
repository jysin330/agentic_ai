from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role": "user", "content": "Hey There!"}
    ]
    
)
print(response.choices[0].message.content)



from google import genai

client_google = genai.Client()
response_google = client_google.models.generate_content(
    model="gemini-3-flash-preview", contents= "Hey There!"
)
print(response_google.text)
