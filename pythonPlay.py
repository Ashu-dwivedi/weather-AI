def get_weather():
    weather = {
        "city": "Delhi",
        "temperature": "30°C"
    }
    return weather
weather_data = get_weather()

print("weather Report")
print(f"city : {weather_data['city']}")
print(f"temperature : {weather_data['temperature']}")
