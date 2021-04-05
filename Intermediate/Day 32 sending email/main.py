##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas
import datetime as dt
import random as rnd
import smtplib


my_email = "ivasik.morozov1999@gmail.com"
password = "qaz123wertfasny"

dates_of_birth = pandas.read_csv("birthdays.csv")
print(type(dates_of_birth))
dates_of_birth_dictionary = {(data["month"], data["day"]): data for(index, data) in dates_of_birth.iterrows()}

now = dt.datetime.now()
month = now.month
day_of_month = now.day

letter_template1=""
letter_template2=""
letter_template3=""

with open("letter_templates/letter_1.txt") as letter1:
    letter_template1=letter1.read()
with open("letter_templates/letter_2.txt") as letter2:
    letter_template2=letter2.read()
with open("letter_templates/letter_3.txt") as letter3:
    letter_template3=letter3.read()

today = (month, day_of_month)
letters_template = [letter_template1, letter_template2, letter_template3]
if today in dates_of_birth_dictionary:
    birthday_person = dates_of_birth_dictionary[today]
    random_letter = rnd.choice(letters_template)
    letter_with_name = random_letter.replace("[NAME],", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        print(letter_with_name)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                                   msg=f"Subject:Happy birthday\n\n {letter_with_name}")

