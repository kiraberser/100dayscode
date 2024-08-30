import requests
from datetime import datetime
import os

APP_ID = os.environ.get("API_ID_EXERCISE")
API_KEY = os.environ.get("API_KEY_EXERCISE")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/14323f5b4818368309b60abfa476057e/workouts/workouts"


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": input("Tell me which exercise you did: ")
}


response = requests.post(url=EXERCISE_ENDPOINT, headers=headers, json=parameters)
data = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    body = {
        "workout": {
            "date": today_date,  # Example date
            "time": now_time,  # Example time
            "exercise": exercise["name"].title(),  # Example exercise
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

response_sheety = requests.post(url=SHEETY_ENDPOINT, json=body, auth=('kiraberser', 'locoloco123'))
print(response_sheety.text)
