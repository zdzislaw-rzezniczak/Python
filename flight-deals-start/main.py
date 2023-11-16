import smtplib
from email.mime.text import MIMEText

from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch

from pprint import pprint

password = "#############"
subject = "Flights"
body = "body"
sender = "zdzichrz@gmail.com"
recipients = ["zdzichrz@gmail.com"]

data_manager = DataManager()
sheet_data = data_manager.get_all_data_from_google_sheet()

flight_search = FlightSearch()

# for destination in sheet_data:
#     if destination['iataCode'] == '':
#         print(destination['city'])
#         destinations_code = flight_search.get_destination_code(destination['city'])
#         destination['iataCode'] = destinations_code
#
# data_manager.update_destination_codes()
#
not_man = NotificationManager()

for destination in sheet_data:
    flight_data = flight_search.get_flights(destination['iataCode'])
    if flight_data.price < destination['lowestPrice']:
        body = f"""
            Wylot z Londyn ->
            Do: {flight_data.destination_city}
            cena: {flight_data.price * 5.02} PLN
            wylot: {flight_data.out_date} 
            powrót: {flight_data.return_date}
        """
        not_man.send_email(subject, body, sender, recipients, password)
