from flask import Blueprint
from src.services.weather_sevice import WeatherService

base_url = Blueprint('temperature', __name__)

@base_url.route("/<string:city>/")
def home(city):
    temp_city = WeatherService()
    temperatura = temp_city.city_temperature(city)
    return temperatura