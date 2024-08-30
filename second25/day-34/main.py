import requests
from twilio.rest import Client
import os

LAT = 19.173773
LNG = -96.134224

account_sid = os.environ.get("TWILIO_ACCOUNT")
auth_token = os.environ.get("TWILIO_API_KEY")

parameters = {
    "lat": LAT,
    "lon": LNG,
    "appid": os.environ.get("OPW_API_KEY"),
    "cnt": 4 #this is equal to 12 hours if you want the weather only for the next 6 houres you can put the number 2
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
data = response.json()

#id = data["list"][0]['weather'][0]['id']

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True
    

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Parece que va a llover hoy, llevate un paraguas o al menos una chamarra",
        from_="+18178359131",
        to=""
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hoy estará soleado, te recomiendo ponerte bloqueador solar",
        from_="18178359131",
        to=""
    )
