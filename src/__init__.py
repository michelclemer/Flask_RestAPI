from flask import Flask, Blueprint
import os
from src.services.weather_sevice import WeatherService


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get('SEVRET_KEY'),
        )
    else:
        app.config.from_mapping(test_config)

    Blueprint('temperature', __name__)


    @app.route("/<string:city>")
    def home(city):
        temp_city = WeatherService()
        temperatura = temp_city.city_temperature(city)
        return temperatura

    return app

