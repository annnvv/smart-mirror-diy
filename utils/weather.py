import requests
import json
from datetime import datetime

# maps open weather icons to weather conditions
# https://openweathermap.org/weather-conditions
icon_lookup = {
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
    "clear-sky": "imgs/Sun.png",  # clear sky day
    "clear-night": "imgs/Moon.png",  # clear sky night
    "clouds": "imgs/Cloud.png",  # cloudy day
    "partly-cloudy-day": "imgs/PartlySunny.png",  # partly cloudy day
    "partly-cloudy-night": "imgs/PartlyMoon.png",  # scattered clouds night
    # 'wind': 'imgs/Wind.png',  # wind
    # 'snow-thin': 'imgs/Snow.png',  # sleet day
    # 'hail': 'imgs/Hail.png',  # hail
}


class Weather:
    def __init__(self):
        self.temp = ""
        self.feels_like = ""
        self.temp_max = ""
        self.temp_min = ""
        self.weather_desc = ""
        self.sunrise = ""
        self.sunset = ""

    def get_weather(self, zip_code: str, weather_api_key: str):
        """
        Method to query the openweathermap API to get current temperature, feels like temperature,
        daily min temperature, daily max temperature, weather conditions, sunrise, and sunset
        """

        weather_req_url = str(
            f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={weather_api_key}&units=imperial"
        )

        try:
            r = requests.get(weather_req_url)
            weather_obj = json.loads(r.text)

        except requests.exceptions.RequestException as e:
            print("Raise error:", e)

        # degree_sign = "\N{DEGREE SIGN}"

        self.temp = str(round(weather_obj["main"]["temp"]))
        self.feels_like = str(round(weather_obj["main"]["feels_like"]))
        self.temp_max = str(round(weather_obj["main"]["temp_max"]))
        self.temp_min = str(round(weather_obj["main"]["temp_min"]))
        self.weather_desc = weather_obj["weather"][0]["main"]
        self.sunrise = datetime.fromtimestamp(weather_obj["sys"]["sunrise"]).strftime(
            "%H:%M"
        )
        self.sunset = datetime.fromtimestamp(weather_obj["sys"]["sunset"]).strftime(
            "%H:%M"
        )

        #         icon_id = weather_obj['currently']['icon']
        #         icon2 = None

        #         if icon_id in icon_lookup:
        #             icon2 = icon_lookup[icon_id]

        #         if icon2 is not None:
        #             if self.icon != icon2:
        #                 self.icon = icon2
        #                 image = Image.open(icon2)
        #                 image = image.resize((100, 100), Image.ANTIALIAS)
        #                 image = image.convert('RGB')
        #                 photo = ImageTk.PhotoImage(image)

        #                 self.iconLbl.config(image=photo)
        #                 self.iconLbl.image = photo
        #         else:
        #             # remove image
        #             self.iconLbl.config(image='')

        # self.after(600000 * 3, self.get_weather)
