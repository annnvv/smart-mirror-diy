import requests
import json
from datetime import datetime
from read_yaml import configData


class Weather(configData):
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
        return None
