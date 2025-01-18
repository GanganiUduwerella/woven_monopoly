import unittest
import os
from game.board import Board, Go, Property
import json


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.test_json_file = 'test_board.json'
        self.test_data = [
            {"name": "GO", "type": "go"},
            {"name": "The Burvale", "price": 1, "colour": "Brown", "type": "property"},
            {"name": "The Grand Tofu", "price": 2, "colour": "Red", "type": "property"}
        ]
        with open(self.test_json_file, 'w') as file:
            json.dump(self.test_data, file)

    def tearDown(self):
        if os.path.exists(self.test_json_file):
            os.remove(self.test_json_file)

    def test_fromJsonFile(self):
        board = Board.fromJsonFile(self.test_json_file)

        self.assertEqual(len(board.spaceList), 3)

        go_space = board.spaceList[0]
        self.assertIsInstance(go_space, Go)
        self.assertEqual(go_space.spaceName, "GO")
        self.assertEqual(go_space.spaceType, "go")
        self.assertEqual(go_space.occupants, []) 

        property_space = board.spaceList[1]
        self.assertIsInstance(property_space, Property)
        self.assertEqual(property_space.spaceName, "The Burvale")
        self.assertEqual(property_space.spaceType, "property")
        self.assertEqual(property_space.spacePrice, 1)
        self.assertEqual(property_space.spaceColour, "Brown")
        self.assertIsNone(property_space.owner)

        another_property = board.spaceList[2]
        self.assertEqual(another_property.spaceName, "The Grand Tofu")
        self.assertEqual(another_property.spacePrice, 2)
        self.assertEqual(another_property.spaceColour, "Red")

   
if __name__ == '__main__':
    unittest.main()
