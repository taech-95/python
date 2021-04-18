import requests

my_email = "ivasik.morozov1999@gmail.com"
password = "password"

api_key = "..."
endpoint = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": 52.237049,
    "lon": 21.017532,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=endpoint, params=params)
response.raise_for_status()
data = response.json()
slicer = data["hourly"][:13]
print(data["hourly"][0]["weather"][0]["id"])
print(slicer)
weather_id =[]
will_rain = False
for hour_data in slicer:
    condition = int(hour_data["weather"][0]["id"])
    if condition < 700:
        weather_id.append(hour_data["weather"][0]["id"])
        will_rain = True

if will_rain:
    print("Bring an umbrella")

print(weather_id)

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     print(letter_with_name)
#     connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
#                         msg=f"Subject:Happy birthday\n\n {letter_with_name}")
