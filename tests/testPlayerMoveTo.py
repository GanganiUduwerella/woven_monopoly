import unittest
from game.player import Player

class TestPlayerMoveTo(unittest.TestCase):
    def test_move_forward_without_passing_go(self):
        player = Player(name="Peter", money=16, currentPosition=0)

        player.moveTo(5)

        self.assertEqual(player.currentPosition, 5)
        self.assertEqual(player.money, 16)

    def test_move_forward_with_passing_go(self):
        
        player = Player(name="Charlotte", money=16, currentPosition=8)

        player.moveTo(2)

        self.assertEqual(player.currentPosition, 2)
        self.assertEqual(player.money, 17)

    def test_move_forward_to_go(self):
        player = Player(name="Billy", money=16, currentPosition=9)

        player.moveTo(0)

        self.assertEqual(player.currentPosition, 0)
        self.assertEqual(player.money, 17)

if __name__ == "__main__":
    unittest.main()
