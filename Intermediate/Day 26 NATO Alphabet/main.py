
import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:

dictionary = {row.letter : row.code for (letter, row) in df.iterrows()}

print(dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()
answer = {dictionary[code] for code in user_input}
print(answer)