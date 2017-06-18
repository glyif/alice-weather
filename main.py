from amoeba.amoeba import env
env.set_env("./.env")
from weather.weather import Weather
from weather.rec_engine.engine import Recommendation


new_weather = Weather()
rec = Recommendation(new_weather)
print("It's {} today, you should wear {}".format(rec.temp_rec, rec.clothing))

