import requests
from bs4 import BeautifulSoup
import smtplib
import os 
from dotenv import load_dotenv
import html
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

MY_EMAIL = os.environ["MY_GMAIL"]
PASSWORD = os.environ["PASSWORD"]
TO_EMAIL = os.environ["TO_GMAIL"]

ENDPOINT = "https://www.amazon.com.mx/El-Libro-rojo-pocket-Espa%C3%B1ola/dp/8412495845/?_encoding=UTF8&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "es-MX,es;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

response = requests.get(url=ENDPOINT, headers=headers)
response_txt = response.text
soup = BeautifulSoup(response_txt, "html.parser")

price = float(soup.find(class_="a-price-whole").get_text().replace(".", "").replace(",", ""))
title = (soup.find(class_="a-size-large celwidget").get_text())


if price < 1100:    
    msg = MIMEMultipart()
    msg['From'] = MY_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = "Amazon Price Alert!! 👋"
    # Cuerpo del mensaje
    body = f"{title} is now ${price}\nCheck it out here: {ENDPOINT}"
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
    with smtplib.SMTP("smtp.gmail.com", 587) as connect:
        connect.starttls()
        connect.login(user=MY_EMAIL, password=PASSWORD)
        connect.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=msg.as_string()
        )