import yagmail
import pandas
from news import NewsFeed
import datetime
import time
import os
import dotenv
dotenv.load_dotenv()
SENDER_EMAIL_PASSWORD = os.getenv('SENDER_EMAIL_PASSWORD')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDING_EMAIL_HOUR = os.getenv('SENDING_EMAIL_HOUR')
SENDING_EMAIL_MINUTE = os.getenv('SENDING_EMAIL_MINUTE')
EXCEL_NAME = os.getenv('EXCEL_NAME')

def send_email():
    """Create a news feed report about user interest and send it in email"""
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    to_email, name, interest = row['email'], row['name'], row['interest']
    print(f"News email sent to {to_email} about {interest}")

    news_feed = NewsFeed(interest={row['interest']},
                         from_date=yesterday,
                         to_date=today,
                         language='en')
    email = yagmail.SMTP(password=SENDER_EMAIL_PASSWORD, user=SENDER_EMAIL)
    email.send(to=to_email,
               subject=f"Your {interest} news for today!",
               contents=f"Hi {name}\nSee what's on about {interest} today. \n{news_feed.get()}\nYuval")


while True:
    if datetime.datetime.now().hour == int(SENDING_EMAIL_HOUR) and datetime.datetime.now().minute == int(SENDING_EMAIL_MINUTE):
        df = pandas.read_excel(EXCEL_NAME)
        df = df.dropna(how='all')  # remove lines that are all 'NaN'
        for index, row in df.iterrows():
            send_email()
        time.sleep(60)

