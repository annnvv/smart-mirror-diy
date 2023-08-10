import yaml


class configData:
    def __init__(self) -> None:
        with open("_auth/config.yaml", "r") as f:
            config = yaml.safe_load(f)

        self._weather_api_key = config["weather"]["api_key"]
        self._weather_zip_code = config["weather"]["zipcode"]
        self._weather_lat = config["weather"]["lat"]
        self._weather_lon = config["weather"]["lon"]

        self._wmata_api_key = config["wmata"]["api_key"]
        self._wmata_station_code = config["wmata"]["station_code"]

        # self._dash_bus_number = config["dash"]["bus_number"]
        # self._dash_stop_numbers = config["dash"]["stop_numbers"]
