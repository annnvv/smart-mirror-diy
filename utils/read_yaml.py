import yaml


class configData:
    def __init__(self) -> None:
        with open("_auth/config.yaml", "r") as f:
            config = yaml.safe_load(f)

        self._weather_api_key = config["weather"]["api_key"]
        self._weather_zip_code = config["weather"]["zipcode"]

        self._wmata_api_key = config["wmata"]["api_key"]
        self._wmata_station_code = config["wmata"]["station_code"]

        # self.dash_bus_number = config["dash"]["bus_number"]
        # self.dash_stop_numbers = config["dash"]["stop_numbers"]
