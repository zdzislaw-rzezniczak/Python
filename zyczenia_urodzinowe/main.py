import smtplib
from email.mime.text import MIMEText
import datetime as dt
import random
import pandas as pd

password = "##########"
subject = "Birthday wishes"
body = "body"
sender = "zdzichrz@gmail.com"
recipients = ["zdzichrz@gmail.com"]


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

try:
    df = pd.read_csv("birthdays.csv")

except FileNotFoundError:
    print("brak pliku birthdays.csv ")
    exit(-1)
today = dt.datetime.now()
dates = []

num_of_rows = len(df)


for n in range(num_of_rows):
    date = dt.datetime(df['year'][n], df['month'][n], df['day'][n])
    if today.month == date.month and today.day == date.day:
        random_int = random.randint(1, 3)
        try:
            with open(f"letter_templates/letter_{random_int}.txt") as file:
                new_letter = file.read().replace("[NAME]", f"{df['name'][n]}")

        except FileNotFoundError:
            print(f"niestety nie ma takiego pliku letter_{random_int}.txt")
            exit(-1)

        body = new_letter
        recipients = [df['email'][n]]
        send_email(subject, body, sender, recipients, password)


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
