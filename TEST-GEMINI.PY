from google import genai
import os
api_key = os.getenv("GEMINI_API_KEY")
print("API key found:", bool(api_key))
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
   model="gemini-3.6-flash",
   contents="Say hello in one sentence"
)
print(response.text)