import requests
import os
from src.config.conf_ import ConfigEnv


class WeatherService:
    def __init__(self):
        self.req = requests

    def city_temperature(self, city_name: str) -> dict:
        resp = self.req.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, ConfigEnv.api_key))
        return resp.json()



