import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "9806f940b9e5d62feff06496bb5214b7"
account_sid = "AC8141ae23b27acc198f336e6505c53be7"
auth_token = "eb2594f255a70a5659865d2939928ee3"

# Location: Hampankatta, Mangalore
MY_LAT = 12.870660
MY_LONG = 74.843690

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
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂",
        from_='+17472710343',
        to='+917795744005'
    )
    print(message.status)





