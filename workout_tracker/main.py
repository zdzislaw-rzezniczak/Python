import requests
import datetime as dt
import os



APP_ID = os.environ.get('APP_ID')
NUTRIONIX_API_KEY = os.environ.get('NUTRIONIX_API_KEY')
API_ENDPOINT = os.environ.get('API_ENDPOINT')
SHEETY_API_ENDPOINT = os.environ.get('SHEETY_API_ENDPOINT')
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')



headers = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRIONIX_API_KEY,
    "x-remote-user-id": "0",
}

# user_activity_str = input("Tell me whcich excersise you did: ")

nutrionix_data = {
    "query": "Run for 5 km",
    "gender": "male",
    "weight_kg": 112,
    "height_cm": 185,
    "age": 41
}

response = requests.post(url=API_ENDPOINT, headers=headers, json=nutrionix_data)
data = response.json()["exercises"][0]
print(data)
exercise = data['name']
date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%H:%M:%S")
duration = data['duration_min']
calories = data['nf_calories']

data_json = {
    "sheet1": {
        "exercise": exercise,
        "date": date,
        "time": time,
        "duration": duration,
        "calories": calories
    }
}

headers_sheety = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}
response = requests.post(url=SHEETY_API_ENDPOINT, json=data_json, headers=headers_sheety)
print(response.text)