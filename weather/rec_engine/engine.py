from weather.weather import Weather

class Recommendation:
    
    def __init__(self, weather_class):
        self.my_weather = weather_class
        self.wear()

    def wear(self):
        temp = self.my_weather.avg_temp
        if temp < 30:
            self.temp_rec = "cold"
            self.clothing = "heavy coat"
        elif temp >= 30 and temp < 50:
            self.temp_rec = "chilly"
            self.clothing  = "jacket and long pants"
        elif temp >= 50 and temp < 75:
            self.temp_rec = "right"
            self.clothing = "t-shirt and shorts"
        elif temp >= 75 < 85:
            self.temp_rec =  "warm"
            self.clothing = "t-shirt and shorts"
        elif tmp >= 85:
            self.temp_rec = "hot"
            self.clothing = "t-shirt and shorts"
