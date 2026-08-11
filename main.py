import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

owm_endpoint = os.getenv("OWM_ENDPOINT")
api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

weather_params = {
    "lat": 12.3,
    "lon": 76.6,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()["list"]

will_rain = False
for hour_data in weather_data:
    weather_code = int(hour_data["weather"][0]["id"])
    if weather_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today! Remember to bring an umbrella ☂️",
        from_="+19803500451",
        to="+914382438263"
    )