import smtplib
from email.mime.text import MIMEText
import datetime as dt
import random

password = "############"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


now = dt.datetime.now()
day = now.weekday()

with open("../cytaty_mail/quotes.txt") as file:
    quotes = lines = [line.rstrip() for line in file]

random_quote_nmbr = random.randint(0, len(quotes) - 1)
random_quote = quotes[random_quote_nmbr]

subject = "Quotes"
body = random_quote
sender = "zdzichrz@gmail.com"
recipients = ["zdzichrz@gmail.com"]

if day == 2:
    send_email(subject, body, sender, recipients, password)
