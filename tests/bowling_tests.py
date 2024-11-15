import unittest

from src import bowling


class TestBowling(unittest.TestCase):
    def setUp(self):
        self.game = bowling.Bowling()

    def test_all_gutters(self):
        for i in range(20):
            self.game.roll(0)

        self.assertEqual(self.game.score(), 0)  # add assertion here

    def test_all_ones(self):
        for i in range(20):
            self.game.roll(1)

        self.assertEqual(self.game.score(), 20)

    def test_spares(self):
        self.game.roll(3)
        self.game.roll(7)
        self.game.roll(4)

        for i in range(17):
            self.game.roll(0)

        self.assertEqual(18, self.game.score())


if __name__ == '__main__':
    unittest.main()
