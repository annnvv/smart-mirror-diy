import requests
import json
from datetime import datetime
from read_yaml import configData


class Weather(configData):

    # maps open weather icons to weather conditions, see https://openweathermap.org/weather-conditions
    ##TODO: (low priority)implement logic for clear day/night and cloudly day/night (something having to do with sunrise or sunset)
    __icon_lookup = {
        "clear": "imgs/Sun.png",
        # "clear-sky": "imgs/Sun.png",  # clear sky day
        # "clear-night": "imgs/Moon.png",  # clear sky night
        "clouds": "imgs/Cloud.png",  # cloudy day
        # "partly-cloudy-day": "imgs/PartlySunny.png",  # partly cloudy day
        # "partly-cloudy-night": "imgs/PartlyMoon.png",  # scattered clouds night
        "thunderstorm": "imgs/Storm.png",  # thunderstorm
        "drizzle": "imgs/Rain.png",  # rain day
        "rain": "imgs/Rain.png",  # rain day
        "snow": "imgs/Snow.png",  # snow day
        "mist": "imgs/Haze.png",
        "smoke": "imgs/Haze.png",
        "haze": "imgs/Haze.png",
        "dust": "imgs/Haze.png",
        "fog": "imgs/Haze.png",  # fog day
        "sand": "imgs/Haze.png",
        "ash": "imgs/Haze.png",
        "squall": "imgs/Haze.png",
        "tornado": "imgs/Tornado.png",  # tornado
    }

    def get_weather(self) -> None:
        """
        Method to query the openweathermap API to get current temperature, feels like temperature,
        daily min temperature, daily max temperature, weather conditions, sunrise, and sunset

        Args:
            None, weather_zip_code and weather_api_key are inherited from configData
        Returns:
            None
        """

        ## Make GET request
        weather_req_url = str(
            f"https://api.openweathermap.org/data/2.5/weather?zip={self.weather_zip_code}&appid={self.weather_api_key}&units=imperial"
        )

        try:
            r = requests.get(weather_req_url)
            weather_obj = json.loads(r.text)
            # print(weather_obj)
        except requests.exceptions.RequestException as e:
            print("Raise error:", e)

        ## Parse data from request
        ##TODO: (low priority) maybe created a different instance method to parse the data??
        self.temp = str(round(weather_obj["main"]["temp"]))
        self.feels_like = str(round(weather_obj["main"]["feels_like"]))
        self.temp_max = str(round(weather_obj["main"]["temp_max"]))
        self.temp_min = str(round(weather_obj["main"]["temp_min"]))

        self.weather_desc = weather_obj["weather"][0]["main"]
        self.img_path = self.__icon_lookup[self.weather_desc.lower()]

        self.sunrise = datetime.fromtimestamp(weather_obj["sys"]["sunrise"]).strftime(
            "%H:%M"
        )
        self.sunset = datetime.fromtimestamp(weather_obj["sys"]["sunset"]).strftime(
            "%H:%M"
        )
        return None
