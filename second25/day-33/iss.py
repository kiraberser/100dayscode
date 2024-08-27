import requests
from datetime import datetime
import smtplib
import time

LAT = 19.173773
LNG = -96.134224

MY_EMAIL = "edwinvega3106@gmail.com"
PASSWORD = "zyxuoqcrctyzfjif"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if 14 <= iss_latitude <= 24 and LNG-5 <= iss_longitude <= LNG+5:
        return True

def is_night():
    parameters = {
        "lat": LAT,
        "lng": LNG,
        "tzid": "America/Mexico_City",
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)    
    if is_iss_overhead and is_night:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="edwinfutbol31@gmail.com",
                msg="Subject: Look up\n\n The ISS is above you in the sky".encode('utf-8')
            )

