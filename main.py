import requests
API_KEY = ""
OWM_Endpoint = "api.openweathermap.org/data/2.5/forecast"

LAT = 51.507351
LON = -0.127758

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
}

respone = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
respone.raise_for_status()
print(respone)
data = respone.json()
print(data)


