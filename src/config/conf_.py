import os

class ConfigEnv:
    api_key = os.environ.get('API_KEY')
    secret_key = os.environ.get('SECRET_KEY')
    cache_ttl = os.environ.get('CACHE_TTL')
    default_max_number = os.environ.get('DEFAULT_MAX_NUMBER')
