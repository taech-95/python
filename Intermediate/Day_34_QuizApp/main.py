from Intermediate.Day_34_QuizApp.question_model import Question
from Intermediate.Day_34_QuizApp.quiz_brain import  QuizBrain
from Intermediate.Day_34_QuizApp.data import question_data
from Intermediate.Day_34_QuizApp.ui import UserInteface


question_bank = []



# print(question_data["results"])
for question in question_data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = UserInteface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()
#
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
