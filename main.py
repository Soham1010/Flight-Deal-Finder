import requests
import os
from sheets import FlightDeals
from pprint import pprint
from sheets import city_price
from twilio.rest import Client
from dotenv import load_dotenv
from req_token import InitializeToken

load_dotenv()  # Load environment variables from .env file

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("ACCOUNT_TOKEN")

# Initializing Token Generation
token = InitializeToken()
new_token = token.get_access_token()

# Creating a Flight_deals Object
flight_deals = FlightDeals()

# Get the city-price dictionary
cities = flight_deals.city_price_dict()


URL = f"https://test.api.amadeus.com/v1/shopping/flight-destinations"

parms = {
    "origin": "LON",
    "maxPrice": 1000
}

headers = {
    # Update Authentication Token here
    'Authorization': f'Bearer {auth_token}'
}

try:
    response = requests.get(url=URL, params=parms, headers=headers)
    flight_data = response.json()

    destination_info = [des for des in flight_data["data"]]
    # print(destination_info)

    for i in destination_info:
        if i["destination"] in cities:
            if float(i["price"]["total"]) < cities[i["destination"]]:
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                from_="+14155238886",
                body=f"Lower Price Alert: Destination {i["destination"]}  Price {i["price"]}",
                to="+17164631835",
                )
                print(message.status)

    print(response.status_code)
except:
    print(response.status_code)

