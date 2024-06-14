# QuestionPopper Class
# Commenced 03/07/2022
#
import random
import math
from Difficulty import Difficulty


class QuestionPopper:
    """ Question Popper Class """
    difficulty = Difficulty()  # Difficulty Object
    qType = 1  # Question Type Variable

    def __init__(self):
        """ Question Popper Object Constructor """
        print("QuestionPopper Activated")

    def pop_question(self, q_number):
        """ Asks a Question of random type (0 to 3) """
        print("Question ", q_number + 1)

        self.qType = random.randint(0, 3)

        if self.qType == 0:
            answers = self.addition(self.difficulty.addition_difficulty())
        elif self.qType == 1:
            answers = self.subtraction(self.difficulty.subtraction_difficulty())
        elif self.qType == 2:
            answers = self.multiplication(self.difficulty.multiplication_difficulty())
        else:
            answers = self.division(self.difficulty.division_difficulty())

        return self.check_answer(answers)

    def addition(self, difficulty):
        """ addition question function """
        a = random.randint(2, int(difficulty) + 2)
        b = random.randint(1, int(difficulty))

        question = '\t\t\t' + str(a) + ' + ' + str(b) + ' = \n\n\n\n'
        user_answer = int(self.get_input(question))

        correct_answer = a + b
        return user_answer, correct_answer

    def subtraction(self, difficulty):
        """ subtraction question function """
        a = random.randint(5, difficulty + 3)
        b = a - random.randint(2, round(difficulty / 3) + 3)

        question = '\t\t\t' + str(a) + ' - ' + str(b) + ' = \n\n\n\n'

        user_answer = int(self.get_input(question))

        correct_answer = a - b
        return user_answer, correct_answer

    def multiplication(self, difficulty):
        """ multiplication question function """
        difficulty *= 0.5
        a = math.floor(difficulty / 10)  # Extract 1st significant digit
        b = round(difficulty % 10)  # Extract 2nd significant digit

        a = random.randint(a, a + 9)
        b = random.randint(b, b + 9)

        question = '\t\t\t' + str(a) + ' * ' + str(b) + ' = \n\n\n\n'
        user_answer = int(self.get_input(question))

        correct_answer = a * b
        return user_answer, correct_answer

    def division(self, difficulty):
        """ division question function """
        difficulty *= 1.5
        b = random.randint(2, 12)
        a = b * random.randint(2, round(difficulty / 3) + 3)
        question = '\t\t\t' + str(a) + ' / ' + str(b) + ' = \n\n\n\n'
        user_answer = int(self.get_input(question))

        correct_answer = a / b
        return user_answer, correct_answer

    def get_input(self, prompt):  # Get user input and ignore blanks
        """ Gets user inputs while ignoring accidental enter button presses """
        userIn = input(prompt)

        if userIn == '':
            userIn = self.get_input(prompt)

        return userIn

    def set_difficulty(self, difficulty):
        """ set difficulty function """
        self.difficulty = difficulty

    @staticmethod
    def check_answer(answers):
        """ check answer function """
        [user_answer, correct_answer] = answers
        is_correct = user_answer == correct_answer

        print("Answer = ", is_correct)
        return is_correct

    def get_q_type(self):
        """ returns the question type """
        return self.qType
