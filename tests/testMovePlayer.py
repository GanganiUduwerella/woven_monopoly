import unittest
from game.board import Property, Space, Board
from game.player import Player
from game.game import Game

class TestMovePlayer(unittest.TestCase):
    def setUp(self):
        self.spaces = [
            Space("Go", "go"),
            Property("Baltic Avenue", "property", "brown", 6),
            Property("Mediterranean Avenue", "property", "brown", 6),
        ]
        self.board = Board(self.spaces)
        self.player1 = Player(name="Alice", money=16, currentPosition=0)
        self.player2 = Player(name="Bob", money=16, currentPosition=0)
        self.game = Game(self.board, [self.player1, self.player2])

    def test_move_player_to_free_property(self):
        self.game.movePlayer(playerIndex=0, spacesToMove=1)
        self.assertEqual(self.player1.currentPosition, 1)
        self.assertEqual(self.player1.money, 10)
        self.assertEqual(self.board.spaceList[1].owner, self.player1)

    def test_move_player_to_owned_property(self):
        self.board.spaceList[1].owner = self.player2

        self.game.movePlayer(playerIndex=0, spacesToMove=1)
        self.assertEqual(self.player1.currentPosition, 1)
        self.assertEqual(self.player1.money, 10)
        self.assertEqual(self.player2.money, 22)


if __name__ == "__main__":
    unittest.main()
