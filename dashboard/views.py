from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache

from .utils import fetch_weather, fetch_air_quality

import logging

logger = logging.getLogger(__name__)

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
            cache_key = f"weather_data_{city.lower().strip()}"
            cached_data = cache.get(cache_key)

            if cached_data:
                logger.info(f"Cache hit for {city}")
                context = cached_data
                context['city'] = city
            else:
                logger.info(f"Fetching fresh data for {city}")
                weather_data = fetch_weather(city, api_key)

                if "error" in weather_data:
                    context['error'] = weather_data['error']
                else:
                    context['data'] = weather_data
                    if "coord" in weather_data:
                        lat = weather_data["coord"]["lat"]
                        lon = weather_data["coord"]["lon"]
                        
                        aqi_data = fetch_air_quality(lat, lon, api_key)
                        context['aqi'] = aqi_data
                    
                    # Cache the fetched data for 15 minutes (900 seconds)
                    cache.set(cache_key, {'data': context.get('data'), 'aqi': context.get('aqi')}, 900)
                    context['city'] = city
        elif not api_key:
            logger.error("OPENWEATHER_API_KEY is not set.")
            context['error'] = "Server configuration error. Please contact administrator."

    return render(request, 'dashboard/home.html', context)
