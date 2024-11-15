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
        for i in range(10):
            if self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:
                total_score += 10 + self.rolls[roll_index + 2]
            else:
                total_score += self.rolls[roll_index] + self.rolls[roll_index + 1]

            roll_index += 2

        return total_score