import requests
from datetime import datetime

LATTITUDE = 16.641537
LONGITUDE = 74.465096

parameter = {
    "lat": LATTITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

now = datetime.now()
print(now.hour)