class Bowling:
    def __init__(self):
        self._currentScore = 0

    def roll(self, pins):
        self._currentScore += pins
        pass

    def score(self):
        return self._currentScore