import requests
import os

class Weather:
    """
    weather
    """
    api = os.environ.get("OPEN_WEATHER")
    def __init__(self):
        self.location = os.environ.get("MY_LOCATION") + ",us"

    def daily_weather(self):
        daily_url = "http://api.openweathermap.org/data/2.5/forecast/daily"
        payload = {
                "units" : "Imperial",
                "APPID" : Weather.api,
                "zip" : self.location,
                "cnt" : "1"
                }
        request = requests.get(daily_url, params=payload)
        print(request.json())
