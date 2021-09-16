import requests
from twilio.rest import Client

WEATHER_ENDPOINT= "https://api.openweathermap.org/data/2.5/onecall"
WEATHER_API_KEY = ""
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE = ""
SENDTO_PHONE = ""

weather_params = {
    "lat": 35.467560,
    "lon": -97.516426,
    "appid": WEATHER_API_KEY,
    "exclude": "current,minutely,daily"
}


response = requests.get(WEATHER_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    weather_condition_code = hour_data["weather"][0]["id"]
    if int(weather_condition_code) < 700:
        will_rain = True

if will_rain:

    # Send as SMS

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="Bring an umbrella today!",
        from_=TWILIO_PHONE,
        to=SENDTO_PHONE
    )
    print(message.status)
