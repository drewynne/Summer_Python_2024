# Difficulty Class
# Commenced 07/07/2022
#


class Difficulty:
    """ Difficulty class """

    difficultyArray = [4, 4, 4, 4]  # difficulty for each question type
    diff = 1  # time difference (delta/differential) in seconds
    averageTime = 1.0  # Average time to answer question
    consciousnessThreshold = 20.48  # Time for System 1 to solve question automatically

    def __init__(self):
        """ Difficulty object constructor """
        print("Difficulty Object Initialised")

    def set_start_difficulty(self, start_difficulty):
        """ sets start difficulty """
        self.consciousnessThreshold = start_difficulty * 5
        for d in range(0, len(self.difficultyArray)):
            self.difficultyArray[d] = start_difficulty

    def addition_difficulty(self):
        """ returns addition difficulty """
        return self.difficultyArray[0]

    def subtraction_difficulty(self):
        """ returns subtraction difficulty """
        return self.difficultyArray[1]

    def multiplication_difficulty(self):
        """ returns multiplication difficulty """
        return self.difficultyArray[2]

    def division_difficulty(self):
        """ returns division difficulty """
        return self.difficultyArray[3]

    def set_difficulty(self, q_type, elapsed_time):
        """ sets difficulty based on question type and elapsed time """

        self.update_average_time(elapsed_time)
        diff = self.consciousnessThreshold - self.averageTime

        self.difficultyArray[q_type] = 0.0 * diff ** 5 + 0.0 * diff ** 3 + 4.0 * diff
        self.difficultyArray[q_type] = int(self.difficultyArray[q_type])

        if self.difficultyArray[q_type] < 2:
            self.difficultyArray[q_type] = 4

    def update_average_time(self, elapsed_time):
        """ updates average time """
        self.averageTime = self.rolling_average(self.averageTime, elapsed_time)

    @staticmethod
    def rolling_average(average, new_sample):
        """ helper function for rolling average """
        num_samples = 8

        average -= average / num_samples
        average += new_sample / num_samples

        return average
