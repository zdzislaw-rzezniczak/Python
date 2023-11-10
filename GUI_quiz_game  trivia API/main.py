from data import question_data as qd
from question_model import Question
from quiz_brain import QuizBrain
import html
from ui import QuizInterface

question_bank = []
NUMBER_OF_QUESTIONS_PER_QUIZ = 10
for question in qd:
    question = Question(question["question"], question["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# for i in range(0, NUMBER_OF_QUESTIONS_PER_QUIZ):
#     question = quiz.next_question()
#     quiz_ui.canvas.itemconfig(quiz_ui.question_txt, text=question)

    # answer = input(f"{html.unescape(question.text)} True/False? ")
    # quiz.check_answer(answer, question.answer)

# print(f"Twój wynik to: {quiz.score}/{NUMBER_OF_QUESTIONS_PER_QUIZ}")
