import json
from data import question_data as qd
from question_model import Question
from quiz_brain import QuizBrain
import requests

# API_URL = "https://opentdb.com/api.php?amount=10"
# response = requests.get(API_URL)
# data = json.loads(response.text)
# questions = data["results"]
# print(questions)


question_bank = []
NUMBER_OF_QUESTIONS_PER_QUIZ = 10
for question in qd:
    question = Question(question["text"], question["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
for i in range(0, NUMBER_OF_QUESTIONS_PER_QUIZ):
    question = quiz.next_question()
    answer = input(f"{question.text} True/False? ")
    quiz.check_answer(answer, question.answer)

print(f"Twój wynik to: {quiz.score}/{NUMBER_OF_QUESTIONS_PER_QUIZ}")
