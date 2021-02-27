from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global reps
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    progress_label.config(text="")
    start_button.config(state=ACTIVE)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    if reps % 2 == 1:
        countdown_mechanism(work_time)
        timer_label["text"] = "Work HARD !!!"

    elif reps == 8:
        countdown_mechanism(long_break_time)
        timer_label["text"] = "Long Break :)"
        timer_label.config(fg=RED)
    elif reps % 2 == 0:
        countdown_mechanism(short_break_time)
        timer_label["text"] = "Short Break"
        timer_label.config(fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown_mechanism(counter):
    start_button.config(state=DISABLED)
    count_min = math.floor(counter / 60)
    count_sek = counter % 60
    if count_sek < 10:
        count_sek = f"0{count_sek}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sek}")
    if counter > 0:
        global my_timer
        my_timer = window.after(1000, countdown_mechanism, counter - 1)
    else:
        start_timer()
        marks = ""
        for _ in math.floor(range(reps / 2)):
            marks += "✔"
        progress_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.minsize(height=450, width=350)
window.maxsize(height=450, width=350)
window.config(padx=25, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 24, "bold"), bg=YELLOW, fg=GREEN)
timer_label.pack()
canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)

background = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack(padx=(25, 25))

start_button = Button(text="Start", width=10, highlightthickness=0, command=start_timer)
start_button.pack(side=LEFT)
reset_button = Button(text="Reset", width=10, highlightthickness=0, command=reset_time)
reset_button.pack(side=RIGHT)

progress_label = Label(font=(FONT_NAME, 18, "bold"), bg=YELLOW, fg=GREEN)
progress_label.pack(side=BOTTOM)

window.mainloop()
