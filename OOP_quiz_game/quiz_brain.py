import random
from random import Random


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.numbers = list(range(0, len(question_list)))
        self.score = 0

    # def next_question(self):
    #
    # self.question_number = random.randint(0, len(self.question_list) - 1)
    # if self.question_number in self.numbers:
    #     self.next_question()
    # self.numbers.append(self.question_number)
    # question = self.question_list[self.question_number]
    # return question

    def next_question(self):
        self.question_number = random.choice(self.numbers)
        # print(self.question_number)
        # print(self.numbers)
        self.numbers.remove(self.question_number)
        question = self.question_list[self.question_number]

        return question

    def check_answer(self, players_answer, correct_answer):
        if players_answer.capitalize() == correct_answer:
            print("Super trafiłeś")
            self.score += 1
        else:
            print("Żle")
        print(f"Poprawna odpowiedź {correct_answer}")