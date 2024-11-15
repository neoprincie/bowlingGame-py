import unittest

from src import bowling


class TestBowling(unittest.TestCase):
    def setUp(self):
        self.game = bowling.Bowling()

    def test_all_gutters(self):
        for i in range(20):
            self.game.roll(0)

        self.assertEqual(0, self.game.score())  # add assertion here

    def test_all_ones(self):
        for i in range(20):
            self.game.roll(1)

        self.assertEqual(20, self.game.score())

    def test_spares(self):
        self.game.roll(3)
        self.game.roll(7)
        self.game.roll(4)

        for i in range(17):
            self.game.roll(0)

        self.assertEqual(18, self.game.score())

    def test_strikes(self):
        self.game.roll(10)
        self.game.roll(5)
        self.game.roll(3)

        for i in range(16):
            self.game.roll(0)

        self.assertEqual(26, self.game.score())


if __name__ == '__main__':
    unittest.main()
