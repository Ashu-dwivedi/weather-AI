from dotenv import load_dotenv
from google import genai
import os
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_weather():
   weather = {
       "city": "Delhi",
       "temperature": 32,
       "humidity": 65,
       "condition": "Partly Cloudy",
       "wind_speed": 12
   }
   return weather

weather = get_weather()
prompt = f"""
You are a friendly weather assistant.
Give a short and simple weather report based ONLY on this data:
City: {weather['city']}
Temperature: {weather['temperature']}°C
Humidity: {weather['humidity']}%
Condition: {weather['condition']}
Wind Speed: {weather['wind_speed']} km/h
"""
response = client.models.generate_content(
   model="gemini-3.6-flash",
   contents=prompt
)
print(response.text)