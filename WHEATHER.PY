import requests

def get_weather(city, api_key):
    """Fetch weather data for a given city using the OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    print("Welcome to the Simple Weather App!")
   
    city = input("Enter the city name: ")
    
    # OpenWeatherMap API key
    api_key = "PUT YOUR API"

    weather_data = get_weather(city, api_key)
    
    if weather_data:
        print(f"\nCurrent weather in {city}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Failed to get the weather data. Please check the city name or try again later.")

if __name__ == "__main__":
    main()
