import unittest
from game.board import Property, Space, Board
from game.player import Player
from game.game import Game

class TestGameIsOver(unittest.TestCase):
    def setUp(self):
        self.spaces = [
            Space("Go", "go"),
            Property("Baltic Avenue", "property", "brown", 6),
            Property("Mediterranean Avenue", "property", "brown", 6),
        ]
        self.board = Board(self.spaces)
        self.player1 = Player("Alice", 1, 0)
        self.player2 = Player("Bob", 16, 0)
        self.game = Game(self.board, [self.player1, self.player2])

    def test_game_not_over_initially(self):
        self.assertFalse(self.game.gameIsOver())

    def test_game_over_when_player_bankrupt(self):
        self.game.movePlayer(0, 1)
        self.assertTrue(self.game.gameIsOver())

if __name__ == "__main__":
    unittest.main()
