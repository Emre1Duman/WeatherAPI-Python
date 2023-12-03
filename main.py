import requests
API_KEY = ""
OWM_Endpoint = "api.openweathermap.org/data/2.5/forecast"

LAT = 51.507351
LON = -0.127758

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4,
}

respone = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
respone.raise_for_status()
print(respone)
weather_data = respone.json()

#Loop through next 12 hours
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")




