from amoeba.amoeba import env
env.set_env("./.env")
from weather.weather import Weather


new_weather = Weather()

print(new_weather.location)
print(Weather.api)
new_weather.daily_weather()
