import random
import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

my_name = "Mykola"
new_list = [letter for letter in my_name]
print(new_list)

numbers = range(1, 5)

double_number = [number * 2 for number in numbers]
print(double_number)

names = ["Mykola", "Olenka", "Piotr", " Oksana", "Ania"]
cap_names = [name.upper() for name in names if len(name) >= 5]
print(cap_names)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [number*number for number in numbers]

#Write your code 👆 above:

print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [number for number in numbers if number % 2 == 0]

#Write your code 👆 above:

print(result)

with open("file1.txt") as file1:
  file1_data = file1.readlines()

with open("file2.txt") as file2:
  file2_data = file2.readlines()

result = [int(number) for number in file1_data if number in file2_data]



# Write your code above 👆

print(result)
scores = {name: random.randint(1,100) for name in names}
print(scores)
passes_names = {name:score for(name, score) in scores.items() if score>60}
print(passes_names)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
list_of_words = sentence.split()
# print(list_of_words)
result = {word: len(word) for word in list_of_words}
# Write your code below:

print(result)
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(temp*9/5)+32 for (day, temp) in weather_c.items()}

print(weather_f)




