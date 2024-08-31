import os
import requests
from dotenv import load_dotenv

AMADEUS_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        load_dotenv()
        self._api_key = os.environ['API_KEY']
        self._api_secret = os.environ['API_SECRET']
        self._token = self._get_new_token()
        self.city = []
        
    def _get_new_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        try:
            response = requests.post(url=AMADEUS_ENDPOINT, data=body, headers=headers)
            return response.json()['access_token']
        except KeyError as error:
            return error
    def _get_IATA(self, city_name):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            'keyword': city_name,
            'max': 2,
            "include": "AIRPORTS",
        }
        response = requests.get(url=IATA_ENDPOINT, params=query, headers=headers)
        code = response.json()
        if response.status_code == 200:
            code = response.json()
            if "data" in code and len(code["data"]) > 0:
                return code['data'][0]['iataCode']
            else:
                print(f"No IATA code found for city: {city_name}")
                return "error"
        else:
            print(f"Error {response.status_code}: {response.text}")
    
            