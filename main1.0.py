import requests, os
from twilio.rest import Client

API_KEY = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

LAT = 51.507351
LON = -0.127758

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
print(response)
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])

#Loop through next 12 hours
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Bring an umbrella.',
        from_=os.environ.get("FROM_NUMBER"),
        to=os.environ.get("TO_NUMBER")
)
    
print(message.status)