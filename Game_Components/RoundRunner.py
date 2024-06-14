# RoundRunner Class
# Commenced 03/07/2022
#
import time

from QuestionPopper import QuestionPopper
from Difficulty import Difficulty


class RoundRunner:
    """ Round Runner Class """
    questions_per_round = 10
    difficulty = Difficulty()

    def __init__(self, start_difficulty, questions_per_round):
        """ Round Runner Object Constructor """
        self.difficulty.set_start_difficulty(start_difficulty)
        self.questions_per_round = questions_per_round

    def run_round(self):
        """ Round Run Function, runs 10 questions at per round """
        question_popper = QuestionPopper()

        for i in range(0, self.questions_per_round):

            question_popper.set_difficulty(self.difficulty)
            start_time = time.time()
            is_correct = question_popper.pop_question(i)
            elapsed_time = time.time() - start_time
            if not is_correct:
                elapsed_time = elapsed_time + 1000
                time.sleep(4)

            q_type = question_popper.get_q_type()

            self.difficulty.set_difficulty(q_type, elapsed_time)

            # print(elapsedTime)
