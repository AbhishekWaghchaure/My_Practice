import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 18.460167
MY_LONG = 73.811485

MY_EMAIL = 'abhisw28@gmail.com'
MY_PASSWORD = 'Abhishek@2829'


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    # print(response)
    response.raise_for_status()

    data = response.json()
    # print(data)

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])
    # iss_position = (longitude, latitude)
    # print(iss_position)

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 :
        return True

def is_night():
    parameters = {
        'lat' : MY_LAT,
        'lng' : MY_LONG,
        'formatted' : 0
    }

    api_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    api_response.raise_for_status()
    data = api_response.json()
    print(data)

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    print(sunrise)
    print(sunset)

    time_now = datetime.now()
    print(time_now.hour)
    
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:  
    time.sleep(60)  
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        
        connection.send(
            from_addr = MY_EMAIL,
            to_addrs = MY_EMAIL,
            msg = 'Subject: Look Up ☄️👆🏻\n\nThe ISS is above you in the sky.'
        )