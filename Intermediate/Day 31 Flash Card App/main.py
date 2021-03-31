BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dictionary = original_data.to_dict(orient="records")
else:
    data_dictionary = data.to_dict(orient="split")
my_timer = None
current_card = {}


def generate_card():
    # Version 1
    # random_word = random.randint(0, len(data_dictionary) - 1)
    # list_of_words_french = []
    # list_of_words_english = []
    # for words in data_dictionary:
    #     list_of_words_french.append(words["French"])
    #     list_of_words_english.append(words["English"])
    # random_french_word = list_of_words_french[random_word]
    # random_english_word = list_of_words_english[random_word]
    # print(random_french_word)
    # print(random_english_word)
    # canvas.itemconfig(word_text, text=random_french_word)
    # canvas.itemconfig(title_text, text="French")
    # Version 2
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dictionary)
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(canvas_background, image=background)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_background, image=english_background)

def is_known():
    data_dictionary.remove(current_card)
    data = pandas.DataFrame(data_dictionary)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_card()

window = Tk()
window.title("Flash Card App")
# window.minsize(300, 300)
window.minsize(width=900, height=750)
window["bg"] = BACKGROUND_COLOR
window["padx"] = 50
window["pady"] = 50

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
background = PhotoImage(file="images/card_front.png")
english_background = PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(400, 275, image=background)
canvas.grid(row=1, column=0, pady=20, columnspan=2)
title_text = canvas.create_text(400, 125, text="Title", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 275, text="Word", fill="black", font=("Arial", 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

btn_wrong = Button(image=wrong_image, highlightthickness=0, command=generate_card)
btn_wrong.grid(column=0, row=2)

btn_right = Button(image=right_image, highlightthickness=0, command=is_known)
btn_right.grid(column=1, row=2)
flip_timer = window.after(3000, flip_card)
generate_card()

window.mainloop()
