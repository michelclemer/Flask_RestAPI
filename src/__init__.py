from flask import Flask
import os
from src.services.weather import base_url
from src.config.conf_ import ConfigEnv


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    config = {
        "DEBUG": True,  # some Flask specific configs
        "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
        "CACHE_DEFAULT_TIMEOUT": 30
    }
    if config is None:
        app.config.from_mapping(
            SECRET_KEY=ConfigEnv.secret_key,
        )
    else:
        app.config.from_mapping(config)

    app.register_blueprint(base_url, url_prefix='/temperature')


    return app

