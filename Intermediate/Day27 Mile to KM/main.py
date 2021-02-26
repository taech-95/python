from tkinter import *

window = Tk()
window.config(padx=15, pady=15)
window.minsize(300, 150)
window.maxsize(300, 150)
window.title("Mile to Kilometers Converter")


def miles_to_km():
    mile = int(textbox.get())
    mile = float(mile * 1.609)
    result_label["text"] = mile


textbox = Entry(width=25)
textbox["text"] = 0
textbox.grid(column=2, row=1)

miles_label = Label()
miles_label["text"] = "Miles"
miles_label.grid(column=3, row=1)
equal_label = Label()
equal_label["text"]="is equal to"
equal_label.grid(column=1, row=2)
result_label=Label()
result_label["text"] = 0
result_label.grid(column=2, row=2)
km_label = Label(text="Km")
km_label.grid(column=3, row=2)
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)


window.mainloop()
