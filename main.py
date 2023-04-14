import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.getenv("owm_api_key")
account_sid = os.getenv("twillio_sid")
auth_token = os.getenv("twillio_auth_token")
twillio_verified_no = os.getenv("twillio_verified_no")
twillio_virtual_no = os.getenv("twillio_virtual_token")

MY_LAT = os.getenv("latitude")
MY_LONG = os.getenv("longitude")

parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "exclude":"current,minutely,daily",
    "appid":api_key
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
print(f"Status code: {response.status_code}")
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂",
        from_=twillio_virtual_no,
        to=twillio_verified_no
    )
    print(message.status)





