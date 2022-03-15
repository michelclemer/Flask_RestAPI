
# REST API Flask 

 Weather API  - https://openweathermap.org/api
 
 In the main folder it is necessary to create the file called .env, containing the variables.

## Install

    $ pip install -r requirements.txt
    

## Run the app

    $ flask run


# REST API

The REST API Routes

## Get temperature

### Request

`GET /temperature/<city>`

    curl -i -H 'Accept: application/json' http://localhost:5000/temperature/London/

### Response

    {
      "base": "stations", 
      "clouds": {
        "all": 100
      }, 
      "cod": 200, 
      "coord": {
        "lat": 51.5085, 
        "lon": -0.1257
      }, 
      "dt": 1647351730, 
      "id": 2643743, 
      "main": {
        "feels_like": 287.22, 
        "humidity": 55, 
        "pressure": 1020, 
        "temp": 288.22, 
        "temp_max": 289.34, 
        "temp_min": 287.01
      }, 
      "name": "London", 
      "sys": {
        "country": "GB", 
        "id": 2019646, 
        "sunrise": 1647324902, 
        "sunset": 1647367441, 
        "type": 2
      }, 
      "timezone": 0, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "overcast clouds", 
          "icon": "04d", 
          "id": 804, 
          "main": "Clouds"
        }
      ], 
      "wind": {
        "deg": 80, 
        "speed": 4.63
      }
    }

