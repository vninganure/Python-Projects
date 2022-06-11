import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 16.641537
MY_LONG = 74.465096
MY_MAIL = "vjsmvit@gmail.com"
MY_PASSWORD = "vijay1998"

def is_iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_longitude >= MY_LAT+5 and MY_LONG-5 <= iss_longitude >= MY_LONG+5:
        return True



def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now < sunset and time_now <sunrise:
        return True
while True:
    time.sleep(60)
    if is_night() and  is_iss_above():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_MAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs=MY_MAIL,
                            msg="Subject:Look up\n\nHey, look up iss is your overhead")
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



