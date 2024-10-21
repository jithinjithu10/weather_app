import requests

# API key from OpenWeatherMap
API_KEY = "5cdc85975ffec537c793e8d6f1c043c0"  # Replace with your actual API key

# URL for fetching weather data
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetches weather data for the given city."""
    # Constructing final URL
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    # Making the request
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        # Extracting specific information
        city_name = data["name"]
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Displaying the weather information
        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Error: Could not retrieve weather data. Please check the city name.")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)
 
