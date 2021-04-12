import tkinter
from Intermediate.Day_34_QuizApp.quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class UserInteface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.maxsize(width=400, height=600)
        self.window.minsize(width=350, height=550)
        self.window.config(padx=20, pady=20)
        self.score = tkinter.Label(font=FONT, text=f"{self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)
        self.canvas = tkinter.Canvas(height=250, width=300, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.quiz_text = self.canvas.create_text(150, 125, text="Word", fill=THEME_COLOR, font=FONT, width=275)
        true_image = tkinter.PhotoImage(file="images/true.png")
        false_image = tkinter.PhotoImage(file="images/false.png")
        self.true_btn = tkinter.Button(highlightthickness=0, image=true_image, command=self.true_pressed)
        self.true_btn.grid(column=0, row=2, pady=20)
        self.false_btn = tkinter.Button(highlightthickness=0, image=false_image, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2, pady=20)
        self.window["bg"] = THEME_COLOR
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score} ")
            self.canvas.itemconfig(self.quiz_text, text=q_text)
            self.canvas["bg"] = "white"
        else:
            self.canvas.itemconfig(self.quiz_text, text=" You've reached the end of the quiz")
            self.true_btn.config(state="disable")
            self.false_btn.config(state="disable")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas["bg"] = "green"
        else:
            self.canvas["bg"] = "red"
        self.window.after(1000, self.get_next_question)
