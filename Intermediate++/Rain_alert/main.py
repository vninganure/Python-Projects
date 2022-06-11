import requests

OWM_appId = "ced0d12a3013c26d27209a046a7d0f0c"
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall?"

parameter = {
    "lat": 16.718100,
    "lon": 74.477798,
    "appid": OWM_appId,
    "exclude": "current,minutely,daily,alerts"
}
list_id = []

response = requests.get(ENDPOINT, params=parameter)
response.raise_for_status()
todays_weather = response.json()
day_weather = todays_weather["hourly"][:12]

will_rain = False
for data in day_weather:
    weather_id = data["weather"][0]["id"]
    if weather_id <= 700:
        will_rain = True
if will_rain:
    print("Bring Umbrella")
