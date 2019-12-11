import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/HP-1080p-Intel-i5-8265U-Windows/dp/B07QZNWH3W/ref=pd_sbs_147_1/133-7321397-2365158?_encoding=UTF8&pd_rd_i=B07QZNWH3W&pd_rd_r=eba4f24d-ab01-46eb-8627-604fbad19067&pd_rd_w=o9LNu&pd_rd_wg=TQVoj&pf_rd_p=5873ae95-9063-4a23-9b7e-eafa738c2269&pf_rd_r=ZZQ5GBVYWNT844A5FJEV&psc=1&refRID=ZZQ5GBVYWNT844A5FJEV'

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
    server.login('jamesnjoroge141@gmail.com', 'Traditional.?')

    Subject = 'Alert! Price dropped'
    body = 'check price for hp envy 13 at: PRODUCT URL'
    
    msg = f"Subject: {Subject}\n\n  Body: {body}"

    server.sendmail(
        'jamesnjoroge141@gmail.com',
        'jnjoroge141@gmail.com',
        msg
        )
    print('Email sent')

    server.quit()

while(True):
    checkPrice()
    #runs after every 1hour
    time.sleep(60 * 60)   
