from django.http import JsonResponse
from django.views import View
from django.conf import settings
import requests

class IPView(View):
    def get(self, request):
        visitor_name = request.GET.get('visitor_name', 'Guest')

        # Get client IP
        ip_response = requests.get('https://httpbin.org/ip')
        client_ip = ip_response.json().get('origin')

        # Get location information
        ip_info_url = f"https://ipinfo.io/{client_ip}/json"
        ip_response = requests.get(ip_info_url)
        ip_data = ip_response.json()
        city = ip_data.get('city', 'Unknown')
        location = city


        # Get weather information
        weather_api_key = settings.WEATHER_DATA['WEATHER_API_KEY']
        print(f'weather api: {weather_api_key}')
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        print(f"weather data: {weather_data}")
        temperature = weather_data['main']['temp']

        response_data = {
            "client_ip": client_ip,
            "location": location,
            "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
        }

        return JsonResponse(response_data)
