import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL_ENDPOINT_PUT = 'https://api.sheety.co/14323f5b4818368309b60abfa476057e/flightDeals/prices/'
PASSWORD = os.environ['PASSWORD']
USERNAME = os.environ['USERNAME']

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data1 = []
        self.body = {}
        
    def putData(self):
        id = 2
        for iatacode in self.sheet_data1:
            self.body = {
                "price": {
                    'iataCode': iatacode  
                }
            }
            self.response = requests.put(url=f"{URL_ENDPOINT_PUT}/{id}", json=self.body)
            id += 1
            