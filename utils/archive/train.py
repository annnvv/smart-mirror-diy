from datetime import datetime
import requests
import json
from read_yaml import configData


class Wmata(configData):
    ##TODO3: in order to implement TODO2, need to get station first and last train (API currently not working)
    ##https://www.wmata.com/rider-guide/stations/van-dorn-st.cfm

    # def get_station_open_close(self) -> None:
    #     """Get station information open and close times"""
    #     wmata_req_url = str(
    #         f"https://api.wmata.com/Rail.svc/json/jStationTimes?StationCode={self.wmata_station_code}"
    #     )
    #     headers = {
    #         "api_key": self.wmata_api_key,
    #     }
    #     try:
    #         r = requests.get(wmata_req_url, params=headers)
    #         self.station_obj = json.loads(r.text)

    #     except requests.exceptions.RequestException as e:
    #         print("Error:", e)

    #     return None

    def get_next_train(self) -> None:
        """
        Method that queries the WMATA API to get information about the next train(s) arriving at a station
        Args:
            None; wmata_station_code and wmata_api_key are inherited from configData
        Returns:
            Technically returns None,
            Class has an class variable with a nested list of strings that contain information about the Line, Destination, and Minutes to next train
        """

        ## Make GET request (only when metro station is open)
        wmata_req_url = str(
            f"https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{self._wmata_station_code}"
        )
        headers = {
            "api_key": self._wmata_api_key,
        }

        ##TODO2: (medium priority) limit requests only during when the train is running (note to self: this might be more appropriate in the display/GUI than here)
        current_time = datetime.now().strftime("%H:%M")
        if current_time > "07:00" and current_time < "23:59":
            try:
                r = requests.get(wmata_req_url, params=headers)
                train_obj = json.loads(r.text)

            except requests.exceptions.RequestException as e:
                print("Error:", e)

            ## Parse data from request
            ##TODO1: (low priority) maybe implement this as a dictionary rather than a nested list???
            self.train_info = []
            if train_obj["Trains"]:
                for i in range(len(train_obj["Trains"])):
                    train = [
                        [train_obj["Trains"][i]["Line"]],
                        [train_obj["Trains"][i]["Destination"]],
                        [train_obj["Trains"][i]["Min"]],
                    ]
                    self.train_info.append(train)
        return None
