import requests
from typing import Dict


def fetch_weather(city: str, api_key: str) -> Dict:
    """
    Fetch weather data from OpenWeatherMap API.

    Args:
        city (str): Name of the city to fetch data for.
        api_key (str): OpenWeatherMap API key.

    Returns:
        Dict: JSON response containing weather data or an error message.
    """
    base_url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException:
        return {"error": "Unable to fetch weather data. Please try again."}
    
def fetch_air_quality(lat: float, lon: float, api_key: str) -> Dict:
    """
    Fetch air quality index (AQI) using OpenWeather's Air Pollution API.

    Args:
        lat (float): Latitude of the city.
        lon (float): Longitude of the city.
        api_key (str): OpenWeather API key.

    Returns:
        Dict: JSON response containing AQI and pollutant data,
              or an error message on failure.
    """
    url = (
        "https://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}&lon={lon}&appid={api_key}"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return {"error": "Unable to fetch air quality data."}

