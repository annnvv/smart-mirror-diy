from tkinter import *
import requests
import json
from utils import text, read_yaml


config = read_yaml.read_yaml("_auth/config.yaml")

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


class Weather(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, bg=text.background)
        self.temperature = ""
        # self.forecast = ""
        # self.location = ""
        # self.currently = ""
        # self.icon = ""
        self.degreeFrm = Frame(self, bg=text.background)
        self.degreeFrm.pack(side=TOP, anchor=E)
        self.temperatureLbl = Label(
            self.degreeFrm,
            font=(text.fontH, text.xlarge_text_size),
            fg=text.foreground,
            bg=text.background,
        )
        self.temperatureLbl.pack(side=RIGHT, anchor=N)
        # self.iconLbl = Label(self.degreeFrm, bg=text.background)
        # self.iconLbl.pack(side=RIGHT, anchor=N, padx=20)
        # self.currentlyLbl = Label(
        #     self,
        #     font=(text.fontH, text.medium_text_size),
        #     fg=text.foreground,
        #     bg=text.background,
        # )
        # self.currentlyLbl.pack(side=TOP, anchor=E)
        # self.forecastLbl = Label(
        #     self,
        #     font=(text.fontH, text.small_text_size),
        #     fg=text.foreground,
        #     bg=text.background,
        # )
        # self.forecastLbl.pack(side=TOP, anchor=E)
        # self.locationLbl = Label(
        #     self,
        #     font=(text.fontH, text.small_text_size),
        #     fg=text.foreground,
        #     bg=text.background,
        # )
        # self.locationLbl.pack(side=TOP, anchor=E)
        self.get_weather()

    def get_weather(self, zip_code=None, weather_api_key=None):
        zip_code = config["weather"]["zipcode"]
        weather_api_key = config["weather"]["api_key"]

        weather_req_url = str(
            f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={weather_api_key}&units=imperial"
        )
        r = requests.get(weather_req_url)
        weather_obj = json.loads(r.text)

        degree_sign = "\N{DEGREE SIGN}"

        temperature2 = str(round(weather_obj["main"]["temp"])) + degree_sign
        # feelslike2 = str(round(weather_obj["main"]["feels_like"])) + degree_sign + "F"
        # temp_max = str(round(weather_obj["main"]["temp_max"])) + degree_sign + "F"
        # temp_min = str(round(weather_obj["main"]["temp_min"])) + degree_sign + "F"

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

        #         if self.currently != currently2:
        #             self.currently = currently2
        #             self.currentlyLbl.config(text=currently2)
        #         if self.forecast != forecast2:
        #             self.forecast = forecast2
        #             self.forecastLbl.config(text=forecast2)
        if self.temperature != temperature2:
            self.temperature = temperature2
            self.temperatureLbl.config(text=temperature2)

        #         if self.location != location2:
        #             if location2 == ', ':
        #                 self.location = 'Cannot Pinpoint Location'
        #                 self.locationLbl.config(text='Cannot Pinpoint Location')
        #             else:
        #                 self.location = location2
        #                 self.locationLbl.config(text=location2)
        #     except Exception as e:
        #         traceback.print_exc()
        #         print 'Error: %s. Cannot get weather.' % e

        self.after(600000 * 3, self.get_weather)
