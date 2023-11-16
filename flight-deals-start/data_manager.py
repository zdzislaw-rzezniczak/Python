import os
import requests


SHEETY_API_ENDPOINT = os.environ.get('SHEETY_API_ENDPOINT')
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')

headers_sheety = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_all_data_from_google_sheet(self):
        response = requests.get(url=SHEETY_API_ENDPOINT, headers=headers_sheety)
        self.destination_data = response.json()['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                url=f"{SHEETY_API_ENDPOINT}/{city['id']}",
                json=new_data, headers=headers_sheety
            )
