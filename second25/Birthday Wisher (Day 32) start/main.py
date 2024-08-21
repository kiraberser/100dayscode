import smtplib
import datetime as dt
import random

MY_EMAIL = "edwinvega3106@gmail.com"
PASSWORD = "ivgxhywapbfggdcg"
today = dt.datetime.now()

with open("quotes.txt") as quote:
    data = quote.readlines()
    random_quote = random.choice(data)    
    if today.weekday() == 1:
        with smtplib.SMTP("smtp.gmail.com", 587) as connect:
            connect.starttls()#Transport Layer Security
            connect.login(user=MY_EMAIL, password=PASSWORD)
            connect.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs="edwinfutbol31@gmail.com", 
                msg=f"Subject:Have a great day!!✌️\n\n{random_quote}".encode('utf-8')
            )
