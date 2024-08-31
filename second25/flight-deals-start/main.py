#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData

URL_ENDPOINT = "https://api.sheety.co/14323f5b4818368309b60abfa476057e/flightDeals/prices"

response = requests.get(url=URL_ENDPOINT)
sheet_data = response.json()
data = sheet_data["prices"]

flight_search = FlightSearch()
data_manager = DataManager()
flight_data = FlightData()

for entry in data:
    index = 0
    if entry["iataCode"] == "":
        city_name = entry['city']
        iata_code = flight_search._get_IATA(city_name=city_name)
        if iata_code:
            data[index]["iataCode"] = iata_code
        else:
            sheet_data['iataCode'] = "error11"
        index += 1    

data_manager.sheet_data1 = [iataCode['iataCode'] for index, iataCode in enumerate(data)]

#data_manager.putData()

