import requests
import json
from datetime import datetime


class Weather:
    def __init__(self):
        # self.temp = ""
        # self.feels_like = ""
        # self.temp_max = ""
        # self.temp_min = ""
        # self.weather_desc = ""
        # self.sunrise = ""
        # self.sunset = ""
        self.zip_code = ""
        self.weather_api_key = ""

    ##TODO: Figure out how to pass authentication!
    ##TODO: Figure out how to implement tkinter after method
    @classmethod
    def get_weather(cls) -> None:
        """
        Method to query the openweathermap API to get current temperature, feels like temperature,
        daily min temperature, daily max temperature, weather conditions, sunrise, and sunset

        Args:
            zip_code (str): zipcode
            weather_api_key (str): openweathermap API key
        Returns:
            None
        """

        ## Make GET request
        weather_req_url = str(
            f"https://api.openweathermap.org/data/2.5/weather?zip={cls.zip_code}&appid={cls.weather_api_key}&units=imperial"
        )

        try:
            r = requests.get(weather_req_url)
            weather_obj = json.loads(r.text)

        except requests.exceptions.RequestException as e:
            print("Raise error:", e)

        ## Parse data from request
        cls.temp = str(round(weather_obj["main"]["temp"]))
        cls.feels_like = str(round(weather_obj["main"]["feels_like"]))
        cls.temp_max = str(round(weather_obj["main"]["temp_max"]))
        cls.temp_min = str(round(weather_obj["main"]["temp_min"]))

        cls.weather_desc = weather_obj["weather"][0]["main"]

        cls.sunrise = datetime.fromtimestamp(weather_obj["sys"]["sunrise"]).strftime(
            "%H:%M"
        )
        cls.sunset = datetime.fromtimestamp(weather_obj["sys"]["sunset"]).strftime(
            "%H:%M"
        )
        return None

    # self.after(600000 * 3, self.get_weather)
