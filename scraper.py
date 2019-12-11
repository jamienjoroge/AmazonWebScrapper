import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/HP-Pavilion-Processor-Solid-State-13-an0010nr/dp/B07HBKMLLN/ref=sr_1_6?keywords=hp+envy+14+refurbished&qid=1576050781&sr=8-6'

#get this by typing "my user agent on your browser"
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}

def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    title = soup.find(id="productTitle").getText().strip()
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
    server.login('from_email', 'password')

    Subject = 'Alert! Price dropped'
    body = 'check price for hp envy 13 at: https://www.amazon.com/HP-Pavilion-Processor-Solid-State-13-an0010nr/dp/B07HBKMLLN/ref=sr_1_6?keywords=hp+envy+14+refurbished&qid=1576050781&sr=8-6'
    
    msg = f"Subject: {Subject}\n\n  Body: {body}"

    server.sendmail(
        'from_email',
        'to_email',
        msg
        )
    print('Email sent')

    server.quit()

while(True):
    checkPrice()
    #runs after every 1hour
    time.sleep(60 * 60)   
