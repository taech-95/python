BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas

data = pandas.read_csv("data/french_words.csv")
print(data)
window = Tk()
window.title("Flash Card App")
# window.minsize(300, 300)
window.minsize(width=900, height=750)
window["bg"] = BACKGROUND_COLOR
window["padx"] = 50
window["pady"] = 50

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
background = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 275, image=background)
canvas.grid(row=1, column=0, pady=20, columnspan=2)
title_text = canvas.create_text(400, 125, text="Title", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 275, text="Word", fill="black", font=("Arial", 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

btn_wrong = Button(image=wrong_image, highlightthickness=0)
btn_wrong.grid(column=0,row=2)

btn_right = Button(image=right_image, highlightthickness=0 )
btn_right.grid(column=1,row=2)
window.mainloop()
