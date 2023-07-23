import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" # API key and City variable can be replaced accordingly
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_main = data['weather'][0]['main']
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return {
            'main': weather_main,
            'description': weather_description,
            'temperature': temperature,
            'humidity': humidity
        }
    else:
        print("Failed to fetch weather data.")
        return None

def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = "London"  # Replace with the city name you want to check

    weather_data = get_weather(api_key, city)

    if weather_data:
        print(f"Weather in {city}:")
        print(f"Main: {weather_data['main']}")
        print(f"Description: {weather_data['description']}")
        print(f"Temperature: {weather_data['temperature']} Kelvin")
        print(f"Humidity: {weather_data['humidity']}%")

if __name__ == "__main__":
    main()

# Install "pip install requests"
