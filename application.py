import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
client = os.getenv('client')
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}
url = "https://www.amazon.in/1MORE-Stylish-Dynamic-Bluetooth-Earphone/dp/B07GXKN67F/ref=sr_1_26?keywords=1more&qid=1581270009&s=electronics&sr=1-26"
page = requests.get(url=url, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id="productTitle").get_text().strip()
price = soup.find(id="priceblock_ourprice").get_text().strip()

con_price = int(price.replace(',','')[2:].split('.', 1)[0])
def send_mail():
    server = smtplib.SMTP(host="smtp.mail.yahoo.com", port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL, PASSWORD)
    subject = 'Price fell down!'
    body = 'Check the link:\
    https://www.amazon.in/1MORE-Stylish-Dynamic-Bluetooth-Earphone/dp/B07GXKN67F/ref=sr_1_26?keywords=1more&qid=1581270009&s=electronics&sr=1-26'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(EMAIL, client, msg)
    print('Hey Email has been sent!')
    server.quit()

if (con_price > 3000):
  send_mail()
else:
  print("Price has not dropped!\n")


