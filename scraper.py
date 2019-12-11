import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = '#'

#get this by typing "my user agent on your browser"
headers = {"User-Agent": '#'}

def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    #title = soup.find(id="productTitle").getText().strip()
    price = soup.find(id="priceblock_ourprice").getText().strip()
    converted_price = float(price[1:4])

    if(converted_price < 500.0):
        send_email()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

#you may need to allow less secure app from google
    server.login('#', '#')

    Subject = 'Alert! Price dropped'
    body = 'check price for hp envy 13 at: PRODUCT URL'
    
    msg = f"Subject: {Subject}\n\n  Body: {body}"

    server.sendmail(
        '#',
        '#',
        msg
        )
    print('Email sent')

    server.quit()

while(True):
    checkPrice()
    #runs after every 1hour
    time.sleep(60 * 60)   
