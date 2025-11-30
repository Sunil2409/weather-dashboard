from django.shortcuts import render
from django.conf import settings

from .utils import fetch_weather, fetch_air_quality

import os

api_key = os.getenv("OPENWEATHER_API_KEY")



def home(request):
    """
    Render the home page and show real-time weather data
    based on user input.

    Args:
        request (HttpRequest): Incoming HTTP request.

    Returns:
        HttpResponse: Rendered template with weather context.
    """
    context = {}

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = getattr(settings, 'OPENWEATHER_API_KEY', '')

        if city and api_key:
            weather_data = fetch_weather(city, api_key)

            if "coord" in weather_data:
                lat = weather_data["coord"]["lat"]
                lon = weather_data["coord"]["lon"]

                aqi_data = fetch_air_quality(lat, lon, api_key)

                context['data'] = weather_data
                context['aqi'] = aqi_data
                context['city'] = city


    return render(request, 'dashboard/home.html', context)
