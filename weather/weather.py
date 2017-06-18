import requests
import os

class Weather:
    """
    weather
    """
    api = os.environ.get("OPEN_WEATHER")
    def __init__(self):
        self.location = os.environ.get("MY_LOCATION") + ",us"
        self.daily_weather()

    def daily_weather(self):
        daily_url = "http://api.openweathermap.org/data/2.5/forecast/daily"
        payload = {
                "units" : "Imperial",
                "APPID" : Weather.api,
                "zip" : self.location,
                "cnt" : "1"
                }
        request = requests.get(daily_url, params=payload)
        self.parse_weather(request.json())
    
    def parse_weather(self, full_json):
        full_list = list(full_json.get("list"))
        taken_json = full_list[0].copy()
        self.temp = taken_json.get("temp")
        self.weather = taken_json.get("weather")
        self.weather = self.weather[0].copy()
        self.weather_main = self.weather.get("main")
        self.weather_description = self.weather.get("description")
        self.weather_id = self.weather.get("id")
        self.avg_temp = self.temp.get("day")
