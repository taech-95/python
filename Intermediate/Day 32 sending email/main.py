import smtplib
import datetime as dt
import random as rnd
my_email = "ivasik.morozov1999@gmail.com"
password = "password"


# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="ivasik.morozov32@yahoo.com",
#                     msg="Subject:Hello\n\n This is the body of my email")
# connection.close()
# # ivasik.morozov32@gmail.com
#


now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()
if year == 2021:
    print("Still wearing mask")

date_of_birth = dt.datetime(year=1995, month=1, day=8, hour=8, minute=55)
print(date_of_birth)

quotes = []

with open("quotes.txt") as file:
    quotes = file.readlines()
message = rnd.choice(quotes)
print(day_of_the_week)
print(message)
if(day_of_the_week == 1):
    with smtplib.SMTP("smtp.gmail.com") as connection:
         connection.starttls()
         connection.login(user=my_email, password=password)
         connection.sendmail(from_addr=my_email, to_addrs="ivasik.morozov32@yahoo.com",
                                msg=f"Subject:Motivation\n\n {message}")

# # ivasik.morozov32@gmail.com