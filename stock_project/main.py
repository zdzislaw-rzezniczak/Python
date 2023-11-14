import smtplib
from email.mime.text import MIMEText
import os

import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


subject = "News"
body = ""
sender = "zdzichrz@gmail.com"
recipients = ["zdzichrz@gmail.com"]

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

password = os.environ.get('GOOGLE_PASS')
API_KEY_ALPHAVANTAGE_NEWS = os.environ.get('API_KEY_ALPHAVANTAGE_NEWS')
NESW_API_KEY = os.environ.get('NESW_API_KEY')


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={API_KEY_ALPHAVANTAGE_NEWS}'
r = requests.get(url)
data = r.json()["Time Series (Daily)"]
print(data)
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = float(data_list[0]['4. close'])

day_before_yesterday_closing_price = float(data_list[1]['4. close'])

positive_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)

medium = (yesterday_closing_price + day_before_yesterday_closing_price) / 2
percentege_difference = positive_difference / medium * 100

if percentege_difference > 5:
    print("Get News")

parameters = {
    "q": COMPANY_NAME,
    "apiKey": NESW_API_KEY,
}

news_response = requests.get(NEWS_ENDPOINT, params=parameters)
print(news_response.json())
articles = news_response.json()["articles"]

top_three = articles[:3]
print(top_three)

## SEND ARTICLE VIA EMAIL

with open("news.txt", mode="w", encoding="utf-8") as file:
    for item in top_three:
        file.write(f"Title: {item['title']}: \n")
        file.write(f"Brief: {item['description']}: \n")
        file.write(f"Url: {item['url']}: \n")
        file.write("\n\n")

with open("news.txt", mode="r", encoding="utf-8") as file:
    news = file.read()

send_email(subject, news, sender, recipients, password)
