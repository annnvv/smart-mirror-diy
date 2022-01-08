import requests
import json
from utils.read_yaml import configData


class Wmata(configData):
    def get_next_train(self):
        """
        Method that queries the WMATA API to get information about the next train(s) arriving at a station
        Args:
            None; wmata_station_code and wmata_api_key are inherited from configData
        Returns:
            A list of strings that contain information about the Line, Destination, and Minutes to next train
        """

        ## Make GET request
        ##TODO: limit requests only during when the train is running
        wmata_req_url = str(
            f"https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{self.wmata_station_code}"
        )
        headers = {
            "api_key": self.wmata_api_key,
        }

        try:
            r = requests.get(wmata_req_url, params=headers)
            train_obj = json.loads(r.text)

        except requests.exceptions.RequestException as e:
            print("Error:", e)

        ## Parse data from request
        ##TODO: Figure out a different data structure for this data, maybe dictionary?
        train_info = []
        for i in range(len(train_obj["Trains"])):
            train = (
                train_obj["Trains"][i]["Line"]
                + " "
                + train_obj["Trains"][i]["Destination"]
                + " "
                + train_obj["Trains"][i]["Min"]
            )
            train_info.append(train)

        return train_info
