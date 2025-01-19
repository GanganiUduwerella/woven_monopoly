import unittest
from game.board import Space, Board
from game.player import Player
from game.game import Game

class TestGetWinners(unittest.TestCase):
    def setUp(self):
        self.spaces = [
            Space("Go", "go"),
            Space("Free Parking", "special"),
        ]
        self.board = Board(self.spaces)
        self.player1 = Player("Alice", -1, 0)
        self.player2 = Player("Bob", 15, 0)
        self.player3 = Player("Charlie", 16, 0)
        self.game = Game(self.board, [self.player1, self.player2, self.player3])

    def test_single_winner(self):
        winners = self.game.getWinners()
        self.assertEqual(len(winners), 1)
        self.assertEqual(winners[0], self.player3)

    def test_multiple_winners(self):
        self.player2.money = 16
        winners = self.game.getWinners()
        self.assertEqual(len(winners), 2)
        self.assertIn(self.player2, winners)
        self.assertIn(self.player3, winners)

if __name__ == "__main__":
    unittest.main()
