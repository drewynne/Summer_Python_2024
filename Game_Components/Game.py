# Game Class
# Commenced 03/07/2022

from RoundRunner import RoundRunner


class Game:
    """ Game Class """
    startDifficulty = 1

    def __init__(self, start_difficulty):
        """" Game Constructor """
        self.startDifficulty = start_difficulty

    def play_game(self):
        """ Play the game """
        questions_per_round = 10

        round_runner = RoundRunner(self.startDifficulty, questions_per_round)

        while self.loving_it():
            round_runner.run_round()

    @staticmethod
    def loving_it():
        userIn = input("Press 1 to play a round, 0 to stop ")
        if userIn == "1":
            return True
        else:
            return False
