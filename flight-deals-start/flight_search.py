import os
import requests
import datetime as dt

from flight_data import FlightData


API_KEY_TEQUILA = os.environ.get('API_KEY_TEQUILA')
API_ENDPOINT = 'https://api.tequila.kiwi.com/locations/query'
API_SEARCH_ENDPOINT = 'https://api.tequila.kiwi.com/v2/search'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        headers = {"apikey": API_KEY_TEQUILA}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=API_ENDPOINT, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def get_flights(self, city_code):
        now = dt.datetime.now()
        now_str = now.strftime("%d/%m/%Y")
        in_90_days = (now + dt.timedelta(days=90)).strftime("%d/%m/%Y")
        headers = {"apikey": API_KEY_TEQUILA}
        query = {"fly_from": "LON", "fly_to": city_code, "date_from": now_str, "date_to": in_90_days,
                 "nights_in_dst_from": 7, "nights_in_dst_to": 28,
                 "flight_type": "round",
                 "one_for_city": 1,
                 "max_stopovers": 0,
                 "curr": "GBP"}

        response = requests.get(
            url=API_SEARCH_ENDPOINT,
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
