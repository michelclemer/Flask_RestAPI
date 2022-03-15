import requests
import os

class WeatherService:
    def __init__(self):
        self.req = requests

    def city_temperature(self, city_name: str) -> dict:
        resp = self.req.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, os.environ.get('API_KEY')))
        return resp.json()



