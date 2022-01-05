import requests
import json


class Wmata:
    # def __init__(self):
    #     pass

    def get_next_train(self, station_code: str, wmata_api_key: str):
        """
        Method that queries the WMATA API to get information about the next train(s) arriving at a station
        Args:
            station_code (str): a string that indicates the station code
            wmata_api_key (str): API key that must be requested from WMATA
        Returns:
            A list of strings that contain information about the Line, Destination, and Minutes to next train
        """
        ## Make GET request
        ##TODO: limit requests only during when the train is running
        wmata_req_url = str(
            f"https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{station_code}"
        )
        headers = {
            "api_key": wmata_api_key,
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
