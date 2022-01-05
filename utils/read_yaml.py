import yaml


class configData:
    def __init__(self) -> None:
        with open("../_auth/config.yaml", "r") as f:
            config = yaml.safe_load(f)

        self.weather_api_key = config["weather"]["api_key"]
        self.weather_zip_code = config["weather"]["zip_code"]

        self.wmata_api_key = config["wmata"]["api_key"]
        self.wmata_station_code = config["wmata"]["station_code"]

        self.dash_bus_number = config["dash"]["bus_number"]
        self.dash_stop_numbers = config["dash"]["stop_numbers"]
