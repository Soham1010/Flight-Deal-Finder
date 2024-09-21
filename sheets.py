import requests
from pprint import pprint
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class FlightDeals:
    def __init__(self):
        self.url = "https://api.sheety.co/967904ee9fe8cf7c6db7480d06a3bc63/day39CapstoneFlightDeals/prices"
        self.headers = {
            "Authorization": f"Basic {os.getenv('SHEETY_TOKEN')}"
        }

    def city_price_dict(self):
        # Fetch data from the API and return city-price dictionary
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            sheety_data = response.json()
            city_price = {item["iataCode"]: item["highestPrice"] for item in sheety_data["prices"]}
            return city_price
        else:
            return None


# Usage example
# flight_deals = FlightDeals()

# # Get the city-price dictionary
# city_prices = flight_deals.city_price_dict()

