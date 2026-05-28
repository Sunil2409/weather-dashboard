from django.test import TestCase, Client, override_settings
from django.urls import reverse
from unittest.mock import patch
from django.core.cache import cache

@override_settings(CACHES={'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}})
class WeatherDashboardTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = '/'
        cache.clear()

    @patch('dashboard.views.fetch_weather')
    @patch('dashboard.views.fetch_air_quality')
    def test_home_post_valid_city(self, mock_aqi, mock_weather):
        mock_weather.return_value = {
            "name": "London",
            "coord": {"lat": 51.5074, "lon": -0.1278},
            "main": {"temp": 15.0}
        }
        mock_aqi.return_value = {
            "list": [{"main": {"aqi": 1}}]
        }

        with patch('dashboard.views.settings') as mock_settings:
            mock_settings.OPENWEATHER_API_KEY = 'test_key'
            response = self.client.post(self.home_url, {'city': 'London'})

        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.context)
        self.assertIn('aqi', response.context)
        self.assertEqual(response.context['city'], 'London')
        self.assertEqual(response.context['data']['name'], 'London')

    @patch('dashboard.views.fetch_weather')
    def test_home_post_api_error(self, mock_weather):
        mock_weather.return_value = {"error": "Unable to fetch weather data. Please try again later."}

        with patch('dashboard.views.settings') as mock_settings:
            mock_settings.OPENWEATHER_API_KEY = 'test_key'
            response = self.client.post(self.home_url, {'city': 'InvalidCity'})

        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], 'Unable to fetch weather data. Please try again later.')

    def test_home_post_missing_api_key(self):
        with patch('dashboard.views.settings') as mock_settings:
            mock_settings.OPENWEATHER_API_KEY = ''
            response = self.client.post(self.home_url, {'city': 'London'})

        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], 'Server configuration error. Please contact administrator.')
