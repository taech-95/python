from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# print(f"Your password is: {password}")


def generate_password():
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_textbox.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    email = email_textbox.get()
    website = website_textbox.get()
    password = password_textbox.get()
    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showerror("Warning", "Some of Data is missed, please go back and check insert")
    else:
        output = messagebox.askokcancel(title=website, message=f" These are the details entered to a data file:\n Email: {email}, \n Password: {password}")
        if output:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password} \n")
                website_textbox.delete(0, END)
                password_textbox.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(350, 400)
window.maxsize(700, 800)
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
background_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_textbox = Entry(width=35)
website_textbox.grid(column=1, row=1, columnspan=2)
website_textbox.focus()
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_textbox = Entry(width=35)
email_textbox.grid(column=1, row=2, columnspan=2)
email_textbox.insert(0, "mykola@email.ua")
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_textbox = Entry(width=21)
password_textbox.grid(column=1, row=3)

generate_btn = Button(text="Generate Password", width=15, command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2)




window.mainloop()
