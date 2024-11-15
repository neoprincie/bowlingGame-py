class Bowling:
    def __init__(self):
        self._currentScore = 0
        self.rolls = []

    def roll(self, pins):
        self._currentScore += pins
        self.rolls.append(pins)
        pass

    def score(self):
        total_score = 0
        roll_index = 0

        for frame in range(10):
            if self.is_strike(roll_index):
                total_score += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1
            elif self.is_spare(roll_index):
                total_score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            else:
                total_score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2

        return total_score

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10