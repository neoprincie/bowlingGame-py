import unittest

from src import bowling


class TestBowling(unittest.TestCase):
    def test_all_gutters(self):
        game = bowling.Bowling()

        for i in range(20):
            game.roll(0)

        self.assertEqual(game.score(), 0)  # add assertion here

    def test_all_ones(self):
        game = bowling.Bowling()

        for i in range(20):
            game.roll(1)

        self.assertEqual(game.score(), 20)


if __name__ == '__main__':
    unittest.main()
