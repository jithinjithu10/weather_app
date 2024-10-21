# Weather App

A simple Python application that fetches current weather data for a given city using the OpenWeatherMap API. The app provides real-time weather information, including temperature, weather conditions, humidity, and wind speed.

## Features

- Retrieve current weather data for any city.
- Displays temperature in Celsius.
- User-friendly interface to input city names.

## Getting Started

These instructions will help you set up the project on your local machine.

### Prerequisites

- Python 3.x installed on your machine.
- An OpenWeatherMap API key (sign up for free [here](https://openweathermap.org/api)).

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jithinjithu10/weather_app.git
   cd weather_app
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # For Windows
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Open the `weather_app.py` file:**

   - Open `weather_app.py` in your preferred code editor.
   - Replace the placeholder `your_openweather_api_key` with your actual API key.

2. **Run the application:**

   ```bash
   python weather_app.py
   ```

3. **Enter the city name when prompted.**

   Example input:
   ```
   Enter the city name: New York
   ```

4. **View the weather data displayed on the console.**

### Example Output

When you run the app and input a city name, the output will look like this:

```
City: New York
Temperature: 25°C
Weather: clear sky
Humidity: 60%
Wind Speed: 5 m/s
```

### Troubleshooting

- **Error: Could not retrieve weather data. Please check the city name.**
  - Ensure the city name is correct.
  - Verify that your API key is valid.
  - Check your internet connection.

### License

This project is licensed under the MIT License.

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.
